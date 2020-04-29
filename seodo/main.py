import typer
import os
import requests
import csv

from tabulate import tabulate
from os import path

app = typer.Typer()
URL = 'http://116.202.229.150:5000/'


def read_from_file(file_name):
    if not path.exists(file_name):
        raise typer.BadParameter('{0} can not be found, please specify the full path'.format(file_name))
    if file_name.endswith('.txt'):
        with open(file_name, 'r') as file:
            keywords = file.read().split('\n')
            keywords = [keyword.strip('"').strip("'").strip(' ').strip('\n').strip('\t').strip() for keyword in keywords
                        if keyword]
        print(keywords)
        return keywords

    elif file_name.endswith('.csv'):
        with open(file_name, 'r') as file:
            csv_content = file.read().split('\n')
            keywords = [
                keyword.split(',')[0].strip('"').strip("'").strip("`").strip(' ').strip('\n').strip('\t').strip() for
                keyword in csv_content if keyword]
        print(keywords)
        return keywords

    else:
        raise typer.BadParameter('File should be TXT or CSV')


def export_file(export_to_file, final_response, delimiter):
    full_path = ''
    if len(export_to_file.split('/')) == 1:
        save_path = os.getenv('SEO_DO_SAVE_TO')
        if not save_path:
            save_path = os.path.expanduser('~')
        else:
            if not path.exists(save_path):
                raise typer.BadParameter('{0}, No such directory, please check it again'.format(save_path))

        save_path = save_path if save_path.endswith('/') else save_path + '/'
        full_path = save_path + export_to_file
    else:
        save_path = '/'.join(export_to_file.split('/')[:-1])
        if not path.exists(save_path):
            raise typer.BadParameter('{0}, No such directory, please check it again'.format(save_path))
        full_path = export_to_file

    with open(full_path, 'w') as file:
        writer = csv.writer(file, delimiter=delimiter)
        writer.writerows(final_response)


@app.command()
def group(
        api_key: str = typer.Option('', help="Required API key", show_default=True),
        group_type: str = typer.Option("smart", help="Group type", show_default=True),
        keywords: str = typer.Option(None, help="Keywords separated by comma", show_default=True),
        file_name: str = typer.Option(None, help="File which includes keywords, as csv or txt file", show_default=True),
        export_to_file: str = typer.Option(None,
                                           help="File path and name to export to, "
                                                "if only filename specified without a path, "
                                                "default root is {0}. "
                                                "And if environment variable SEO_DO_SAVE_TO is set, "
                                                "passing the file name will be enough. "
                                                "Value of SEO_DO_SAVE_TO env variable is currentlly : {1} ".format(
                                               os.path.expanduser('~'), os.getenv('SEO_DO_SAVE_TO'))),
        delimiter: str = typer.Option(',',
                                      help="Specify a delimiter only if you specified --export-to-file option, defaults to ',' ",
                                      show_default=True),
        data_structure_mode: str = typer.Option('normal', help="Detailed explanation of all modes here \n\n"
                                                               "normal : Each category returned by API will be put into different columns as normal\n\n"
                                                               "nested: we separate each level and get a set of them to eliminate duplication\n\n"
                                                               "single_category: lorem ipsum\n\n"
                                                               "first_two_category: lorem ipsum\n\n"
                                                               "first_three_category: lorem ipsum\n\n"
                                                               "last_category: lorem ipsum\n\n"),
        category_count_each_line: int = typer.Option(0,
                                                     help="You can change this if the output table on terminal does not fit to your screen, there might be multiple lines for each keyword and that's the idea ")

):
    """
    Takes a list of keywords and returns the grouped response in requested format
    """
    # validate and get the inputs, stage 1
    keywords_list = []
    final_response = []
    if not api_key:
        api_key = os.getenv('SEO_DO_API_KEY')
        if not api_key:
            raise typer.BadParameter(
                "Api key is required, either pass it with --api-key option or set environment variable SEO_DO_API_KEY")

    if keywords:
        keywords_list = keywords.split(',')
    elif file_name:
        keywords_list = read_from_file(file_name)
    else:
        raise typer.BadParameter('Keywords required, please pass --keywords or --file-name')

    # fetch the data from the API, stage 2
    if group_type == 'smart':
        response = requests.get(URL + 'smart_group', json={'apiKey': api_key, 'keywords': keywords_list})

    elif group_type == 'commonality':
        response = requests.get(URL + 'commonality', json={'apiKey': api_key, 'keywords': keywords_list})

    elif group_type == 'google-category':
        response = requests.get(URL + 'google_category', json={'apiKey': api_key, 'keywords': keywords_list})

    else:
        raise typer.BadParameter('{0} is not a valid group type option, Try smart, commonality or google-category')

    # manipulate the data as requested, stage 3

    if data_structure_mode == 'normal':
        final_response = [[keyword, *set(groups)] for keyword, groups in response.json()['grouped_data'].items()]

    elif data_structure_mode == 'nested':
        final_response = [[keyword, *{'/'.join(nested_group.split('/')[:index]) for nested_group in groups for index in
                                      range(1, len(nested_group.split('/')) + 1)}] for keyword, groups in
                          response.json()['grouped_data'].items()]

    elif data_structure_mode == 'single_category':
        final_response = [[keyword, *{single_group for group in groups for single_group in group.split('/')}] for
                          keyword, groups in response.json()['grouped_data'].items()]

    elif data_structure_mode == 'first_two_category':
        final_response = [[keyword, *{'/'.join(group.split('/')[:2]) for group in groups if group.count('/') > 0}] for
                          keyword, groups in response.json()['grouped_data'].items()]

    elif data_structure_mode == 'first_three_category':
        final_response = [[keyword, *{'/'.join(group.split('/')[:3]) for group in groups if group.count('/') > 1}] for
                          keyword, groups in response.json()['grouped_data'].items()]

    elif data_structure_mode == 'last_category':
        final_response = [[keyword, *{group.split('/')[-1] for group in groups}] for keyword, groups in
                          response.json()['grouped_data'].items()]

    # provide the required output to user, stage 4
    if not export_to_file:
        if category_count_each_line:
            final_response = [[data[0], *data[index: index + category_count_each_line]] for data in final_response for
                              index in range(1, len(data[1:]) + 1, category_count_each_line)]
        typer.echo(tabulate(final_response))
    else:
        export_file(export_to_file, final_response, delimiter)

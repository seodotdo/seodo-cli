class seodo < Formula
  include Language::Python::Virtualenv

  desc "An SEO cli that help SEO professionals to organize keywords by different grouping algorithms"
  homepage "https://seo.do"
  url "https://github.com/seodotdo/seodo-cli/releases/download/v0.0.13/seodo-0.0.13.tar.gz"
  sha256 "7545d2ebaf43f71e090bc27b61a736cd4b9fc5e3cf8d21a33818830e0dfa36c8"
  head "https://github.com/seodotdo/seodo-cli.git"

  revision 1

  depends_on "python@3"


  resource "certifi" do
    url "https://files.pythonhosted.org/packages/57/2b/26e37a4b034800c960a00c4e1b3d9ca5d7014e983e6e729e33ea2f36426c/certifi-2020.4.5.1-py2.py3-none-any.whl#sha256=1d987a998c75633c40847cc966fcf5904906c920a7f17ef374f5aa4282abd304"
    sha256 "1d987a998c75633c40847cc966fcf5904906c920a7f17ef374f5aa4282abd304"
  end

  resource "chardet" do
    url "https://files.pythonhosted.org/packages/bc/a9/01ffebfb562e4274b6487b4bb1ddec7ca55ec7510b22e4c51f14098443b8/chardet-3.0.4-py2.py3-none-any.whl#sha256=fc323ffcaeaed0e0a02bf4d117757b98aed530d9ed4531e3e15460124c106691"
    sha256 "fc323ffcaeaed0e0a02bf4d117757b98aed530d9ed4531e3e15460124c106691"
  end

  resource "click" do
    url "https://files.pythonhosted.org/packages/dd/c0/4d8f43a9b16e289f36478422031b8a63b54b6ac3b1ba605d602f10dd54d6/click-7.1.1-py2.py3-none-any.whl#sha256=e345d143d80bf5ee7534056164e5e112ea5e22716bbb1ce727941f4c8b471b9a"
    sha256 "e345d143d80bf5ee7534056164e5e112ea5e22716bbb1ce727941f4c8b471b9a"
  end

  resource "future" do
    url "https://files.pythonhosted.org/packages/45/0b/38b06fd9b92dc2b68d58b75f900e97884c45bedd2ff83203d933cf5851c9/future-0.18.2.tar.gz#sha256=b1bead90b70cf6ec3f0710ae53a525360fa360d306a86583adc6bf83a4db537d"
    sha256 "b1bead90b70cf6ec3f0710ae53a525360fa360d306a86583adc6bf83a4db537d"
  end

  resource "idna" do
    url "https://files.pythonhosted.org/packages/89/e3/afebe61c546d18fb1709a61bee788254b40e736cff7271c7de5de2dc4128/idna-2.9-py2.py3-none-any.whl#sha256=a068a21ceac8a4d63dbfd964670474107f541babbd2250d61922f029858365fa"
    sha256 "a068a21ceac8a4d63dbfd964670474107f541babbd2250d61922f029858365fa"
  end

  resource "urllib3" do
    url "https://files.pythonhosted.org/packages/e1/e5/df302e8017440f111c11cc41a6b432838672f5a70aa29227bf58149dc72f/urllib3-1.25.9-py2.py3-none-any.whl#sha256=88206b0eb87e6d677d424843ac5209e3fb9d0190d0ee169599165ec25e9d9115"
    sha256 "88206b0eb87e6d677d424843ac5209e3fb9d0190d0ee169599165ec25e9d9115"
  end

  resource "requests" do
    url "https://files.pythonhosted.org/packages/1a/70/1935c770cb3be6e3a8b78ced23d7e0f3b187f5cbfab4749523ed65d7c9b1/requests-2.23.0-py2.py3-none-any.whl#sha256=43999036bfa82904b6af1d99e4882b560e5e2c68e5c4b0aa03b655f3d7d73fee"
    sha256 "43999036bfa82904b6af1d99e4882b560e5e2c68e5c4b0aa03b655f3d7d73fee"
  end

  resource "tabulate" do
    url "https://files.pythonhosted.org/packages/57/6f/213d075ad03c84991d44e63b6516dd7d185091df5e1d02a660874f8f7e1e/tabulate-0.8.7.tar.gz#sha256=db2723a20d04bcda8522165c73eea7c300eda74e0ce852d9022e0159d7895007"
    sha256 "db2723a20d04bcda8522165c73eea7c300eda74e0ce852d9022e0159d7895007"
  end

  def install
    virtualenv_install_with_resources
  end

  # TODO: Add your package's tests here
end
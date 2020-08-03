#!/usr/bin/env python

import github
import git
import config.version
from pyapikey import get_key

asset_path = "dist/pyflexebs-{}".format(config.version.version_str)
asset_name = "pyflexebs-{}".format(config.version.version_str)
tag = config.version.version_str
tag_message = "version {}".format(config.version.version_str)

repository = git.Repo()
urls_list = list(repository.remotes.origin.urls)
assert len(urls_list) == 1
url = urls_list[0]
repo_name = url.split("/")[1][:-4]
sha = repository.head.object.hexsha

print(sha)
# repository.create_tag(tag)
# repository.remotes.origin.push(tag)

key = get_key("github")
g = github.Github(key)
repo = g.get_user().get_repo(repo_name)
release = repo.create_git_tag_and_release(
    tag=tag,
    tag_message=tag_message,
    release_name=tag,
    release_message=tag_message,
    object=sha,
    type="commit",
)
release.upload_asset(
    path=asset_path,
    label=asset_name,
)


"""
OLD CODE
os.environ["GITHUB_TOKEN"] = key
subprocess.check_call([
    "git",
    "tag",
    config.version.version_str,
])
subprocess.check_call([
    "git",
    "push",
    "--tags",
])
subprocess.check_call([
    "github-release",
    "release",
    "--user",
    "veltzer",
    "--repo",
    "pyflexebs",
    "--tag",
    config.version.version_str,
    "--name",
    "version {}".format(config.version.version_str),
])
subprocess.check_call([
    "github-release",
    "upload",
    "--user",
    "veltzer",
    "--repo",
    "pyflexebs",
    "--tag",
    config.version.version_str,
    "--name",
    "pyflexebs-{}".format(config.version.version_str),
    "--file",
    "dist/pyflexebs-{}".format(config.version.version_str),
])
"""

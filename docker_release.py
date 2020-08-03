#!/usr/bin/env python

import github
import git
import config.version
import config.project
from pyapikey import get_key

name = config.project.project_name
asset_path = "dist/{}-{}".format(
    name,
    config.version.version_str,
)
asset_name = "{}-{}".format(
    name,
    config.version.version_str,
)
tag = config.version.version_str
tag_message = "version {}".format(config.version.version_str)

repository = git.Repo()
urls_list = list(repository.remotes.origin.urls)
assert len(urls_list) == 1
url = urls_list[0]
repo_name = url.split("/")[1][:-4]
sha = repository.head.object.hexsha

repository.create_tag(tag)
repository.remotes.origin.push(tag)

key = get_key("github")
g = github.Github(key)
repo = g.get_user().get_repo(repo_name)
release = repo.create_git_release(
    tag=tag,
    name=tag,
    message=tag,
    target_commitish=sha,
)
release.upload_asset(
    path=asset_path,
    label=asset_name,
)

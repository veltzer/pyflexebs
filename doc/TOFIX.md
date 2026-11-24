# TOFIX

Findings from a code scan on 2026-10-04.

## High

- `src/pyflexebs/main.py:136` - `volume.size < new_size` compares the EBS size in GiB with `new_size` in bytes, so it is always true and the resize is attempted on every check that crosses the watermark; convert both sides to the same unit.
- `src/pyflexebs/main.py:133` - when the increase exceeds `increase_max_gb`, the increment is set to `ConfigAlgo.increase_max_gb` (e.g. 100) as a byte count, not GB, so hitting the cap shrinks the intended increase to ~0 (any growth left comes only from the GB/GiB mix-up below); multiply by the byte size of a GiB.
- `src/pyflexebs/main.py:105` - inside the `shell=True` command, `awk "{print $2}"` / `awk "{print $1}"` are in double quotes, so the shell expands `$2`/`$1` to empty and awk prints whole lines; the backticked `grep` then gets the whole `lvs` line as pattern+filenames and the LVM device lookup is broken. Do the lookup with `lvs`/`pvs` `--noheadings -o` options via an argv list, not a shell pipeline.
- `pyflexebs.spec:6` - `Analysis(['pyflexebs/main.py'])` points at a path that does not exist since the move to `src/` layout (the file is `src/pyflexebs/main.py`), and `block_cipher`/`cipher=` were removed in PyInstaller 6; `Dockerfile:26` and `scripts/build.*.sh` therefore cannot build the executable - fix the path and drop the cipher arguments.
- `Dockerfile:15` - `pip3 install --user` into the system Python on `ubuntu:26.04` is rejected by PEP 668 (externally-managed-environment), so lines 15, 16 and 25 fail; build in a venv (`python3 -m venv`) instead. Same problem in `scripts/build.apt.sh:3`.

## Medium

- `src/pyflexebs/main.py:143` - sizes are converted with `bitmath.Byte(...).to_GB()` (decimal 10^9) but EBS `Size` is in GiB, so every request over-allocates by ~7% and the `volume_max_size` check at line 120 is off by the same factor; use `to_GiB()`.
- `src/pyflexebs/main.py:102` - the LVM detection runs `lvs | grep {p.mountpoint[1:]}` through `shell=True` as root with an unquoted mountpoint, and the grep is a substring match on a mountpoint path (e.g. `mnt/data`) against LV names, which will not match normal LV naming; use `findmnt`/`lsblk -no TYPE` on `p.device` and pass argv lists.
- `src/pyflexebs/main.py:93` - `normalize_device` only maps `sdX`->`xvdX`; on Nitro instances partitions appear as `/dev/nvmeXn1` while EBS attachments report `/dev/sdX`, so `device_to_volume` never matches and the daemon logs "Cannot find device" forever; map NVMe devices to volume ids (the volume id is in the NVMe serial / `/dev/disk/by-id`).
- `pyproject.toml:44` - `pyinstaller`, `pyapikey`, `PyGithub` and `gitpython` (lines 44-47) are runtime dependencies of the published package but only `scripts/docker_release.py` and the build scripts use them, and `pyfakeuse` (line 38) is not imported anywhere; move the script-only ones to the dev group and drop `pyfakeuse`.
- `tera.snippets/main.md.tera:28` - README tells users to run `./build.yum.sh` / `./build.apt.sh` from the repo root, but they live in `scripts/`; and line 34 says the result is `dist/pyflexebs-[VERSION]`, while those scripts produce `dist/pyflexebs` (only `scripts/docker_build.py:46` adds the version).
- `tera.snippets/main.md.tera:94` - the volume-shrinking recipe is inconsistent: it names the big volume `/dev/sdb` but mounts `/dev/xvdf` (line 106), rsyncs from `/mnt/real/` although the big volume was mounted at `/mnt/big` (line 112), and skips step 6; fix the device names and paths.
- `.jenkins-scanner.yml:5` - references a `Jenkinsfile` that does not exist in the repo (CI is GitHub Actions); delete this leftover file and its entry in `rsconstruct.toml:79`.

## Low

- `scripts/docker_release.py:10` - `tag_message` is computed (line 19) but never used, per its own TODO; pass it to `create_tag(tag, message=tag_message)` or drop it.
- `scripts/docker_release.py:25` - `url.split("/")[1][:-4]` only works for `git@github.com:owner/repo.git` remotes; an https remote yields the wrong repo name - parse the URL properly.
- `src/pyflexebs/main.py:24` - `TAG_DONT_RESIZE` is unused (its only use is commented out at lines 75-77); implement the tag check or remove the constant and the dead comments.
- `pyproject.toml:89` - `mypy_path = "src:python:scripts"` names a `python/` directory that does not exist; drop it.
- `rsconstruct.toml:28` - `ruff`/`mypy` (line 32) list `config` and `shellcheck` (line 40) lists `src` and `config` in `src_dirs`, but those folders contain no files of that type; list only the folders that do.

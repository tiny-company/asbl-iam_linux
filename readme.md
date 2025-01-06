# asbl-iam_linux

## Description

This repo contain the ansible role that configure IAM (Identity Access Management) :
- Configure User and assign ssh keys
- Configure Groups
- Configure advanced linux rights using [ACL]()

## Prerequisite

> If this role is run for the first time on a new machine (on which sudo is not installed)
- it must be run with root user (to avoid using sudo for right upgrade)

## Usage

### Use role

- Add the role git source in "requirements.yml" file :
```
  - name: role_name
    scm: git
    src: https://github.com/tiny-company/<repository_name>.git
    version: main
```

- And then use the galaxy command to load the file dependencies :
```
ansible-galaxy install -r requirements.yml
```

- Or manually get the playbook as collection (with ansible-galaxy) :
```
ansible-galaxy collection install https://github.com/tiny-company/<repository_name>.git
```

### Variables

For an exhaustive list of variables check the [defaults](defaults/main.yml)
file. Ideally, all values will have commentaries describing what are their
purposes and by the default value you can tell the type.


## Source :

- [setting file for github template documentation](https://github.com/Josee9988/project-template/blob/master/.github/settings.yml)
- [github-actions contexts](https://docs.github.com/en/actions/learn-github-actions/contexts)


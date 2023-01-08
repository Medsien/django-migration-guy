# django-migration-guy

A GitHub action to automatically fix multiple leaf errors of Django migrations.

This action does **not** install your Django project. It inspects your migration files statically and creates new a migration.

## Inputs

|Input|Description|Default|
|---|---|---|
|`apps_path`|Path of Django app folders relative to repository root.|`.`|
|`strategy`|`create_pr` for creating changes in a pull request.<br>`push` for pushing to current branch.|`create_pr`|
|`labels`|A comma separated list of labels for pull request.|`auto-migration`|


## Usage

Run automatically when there is a new commit on `main` branch:

```yaml
on:
  push:
    branches:
      - main
jobs:
  fix-django-migrations:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: ulasozguler/django-migration-guy@v0.1.1
        with:
          apps_path: '.'
          strategy: 'create_pr'
          labels: 'auto-migration'
```

---

<details>
  <summary>Manual trigger example</summary>

```yaml
on:
  workflow_dispatch:
    inputs:
      apps_path:
        description: 'Apps path'
        required: true
        default: '.'
      strategy:
        type: choice
        description: Strategy
        options: 
        - create_pr
        - push
        default: create_pr
      labels:
        description: A comma separated list of labels for pull request.
        default: auto-migration
jobs:
  fix-migrations:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: ulasozguler/django-migration-guy@v0.1.1
        with:
          apps_path: ${{ inputs.apps_path }}
          strategy: ${{ inputs.strategy }}
          labels: ${{ inputs.labels }}
```
</details>

## Strategy

It is recommended to set `strategy` to `create_pr` as there are cases this action cannot handle. E.g. if same field is updated by two migrations, order of migrations must be decided manually. This action will still create a valid migration, but it may not be the desired one.

### `create_pr`

This option will create a pull request with a generated migration file. Subsequent runs of this action will update the pull request instead of creating a new one. This behaviour has the benefit of creating less migrations. 

### `push`

This option will push a new commit to current branch. The commit is authored by the actor that triggered the action.

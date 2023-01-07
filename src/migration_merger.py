from datetime import datetime
from pathlib import Path

MIG_TEMPLATE = """# Auto-generated merge migration

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
%s
    ]

"""


def get_next_migration_name(migrations):
    number = int(sorted(migrations)[-1].split("_")[0])
    prefix = str(number + 1).zfill(4)
    datestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"{prefix}_merge_auto_{datestamp}.py"


def create_merge_migration_file(app, leave_migrations, apps_path):
    rows = []
    for migration in leave_migrations:
        rows.append(f"        ('{app}', '{migration}'),")

    content = MIG_TEMPLATE % "\n".join(rows)
    filename = get_next_migration_name(leave_migrations)
    filepath = Path(apps_path) / f"{app}/migrations/{filename}"

    with open(filepath, "w") as f:
        f.write(content)

    return filename

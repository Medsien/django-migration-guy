import logging
import os
from datetime import datetime
from pathlib import Path

from django_migration_checker import get_conflicts

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(name)s:%(levelname)s | %(message)s",
)
logger = logging.getLogger("django-migration-guy")

APP_DIR = os.environ.get("APPS_PATH", ".")
logger.debug(f"Working on path: {APP_DIR}")

MIG_TEMPLATE = """# Auto-generated merge migration

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
%s
    ]

"""


def get_next_mig_name(migs):
    number = int(sorted(migs)[-1].split("_")[0])
    prefix = str(number + 1).zfill(4)
    datestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"{prefix}_merge_auto_{datestamp}.py"


def create_merge_migration_file(app, leave_migs):
    rows = []
    for mig in leave_migs:
        rows.append(f"        ('{app}', '{mig}'),")

    content = MIG_TEMPLATE % "\n".join(rows)
    filename = get_next_mig_name(leave_migs)
    filepath = Path(APP_DIR) / f"{app}/migrations/{filename}"

    with open(filepath, "w") as f:
        f.write(content)

    return filename


def run():
    res = get_conflicts(APP_DIR)

    if not res:
        logger.info("No conflicts detected.")
        return

    for app, conflicts in res:
        logger.info(f"Conflicts in '{app}'")
        logger.info(f"Merging leaves: {','.join(conflicts)}")
        filename = create_merge_migration_file(app, conflicts)
        logger.info(f"Created: {filename}")


if __name__ == "__main__":
    run()
    with open("asd.txt", "w") as f:
        f.write("new stuff")

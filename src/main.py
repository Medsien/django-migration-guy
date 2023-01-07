import logging
import os

from django_migration_checker import get_conflicts

from migration_merger import create_merge_migration_file

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(name)s:%(levelname)s | %(message)s",
)
logger = logging.getLogger("django-migration-guy")

APPS_PATH = os.environ.get("APPS_PATH", ".")
logger.debug(f"Working on path: {APPS_PATH}")


def run():
    res = get_conflicts(APPS_PATH)

    if not res:
        logger.info("No conflicts detected.")
        return

    for app, conflicts in res:
        logger.info(f"Conflicts in '{app}'")
        logger.info(f"Merging leaves: {','.join(conflicts)}")
        filename = create_merge_migration_file(app, conflicts, APPS_PATH)
        logger.info(f"Created: {filename}")


if __name__ == "__main__":
    run()

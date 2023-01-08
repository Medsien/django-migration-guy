import logging
import os

from django_migration_checker import get_conflicts

import github
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

    summary = ""
    for app, conflicts in res:
        logger.info(f"Conflicts in '{app}'. Merging leaves: {','.join(conflicts)}")
        summary += f"Merged migrations of `{app}` app:\n"
        summary += "\n".join([f"- {x}" for x in conflicts])
        summary += "\n"
        filename = create_merge_migration_file(app, conflicts, APPS_PATH)
        logger.info(f"Created: {filename}")

    github.add_output("pr_message", summary)
    github.add_summary(summary)


if __name__ == "__main__":
    run()

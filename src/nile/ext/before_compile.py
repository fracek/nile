"""Example callback for the nile.before_compile entry-point."""
from shutil import copy


def log_file_before_compile(contract):
    print(f"I'm about to compile {contract}")


def make_backup_copy_of_contract(contract):
    copy(contract, f'{contract}.bak')
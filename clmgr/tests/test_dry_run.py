import filecmp
import os
import shutil

from clmgr.main import main


test_dir = os.path.dirname(os.path.realpath(__file__))


def test_dry_run_does_not_modify_files_and_prints_action(capsys):
    directory = "default/py/"
    filename = "single.py"

    input_file = test_dir + "/input/" + directory + filename
    temp_file = test_dir + "/temp/" + directory + filename

    os.makedirs(test_dir + "/temp/" + directory, exist_ok=True)
    shutil.copy(input_file, temp_file)
    shutil.copystat(input_file, temp_file)

    test_args = [
        "-c",
        test_dir + "/config/default/single.yml",
        "--file",
        temp_file,
        "--dry-run",
    ]

    main(test_args)

    out = capsys.readouterr().out
    assert ("inserted copyright" in out) or ("update copyright" in out)
    assert filecmp.cmp(input_file, temp_file, shallow=False)

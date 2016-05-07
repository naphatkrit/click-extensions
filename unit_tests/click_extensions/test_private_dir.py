import os
import pytest

from click_extensions import private_dir


def test_ensure_private_dir_exists():
    assert not os.path.exists(private_dir.private_dir_path('app-name'))
    private_dir.ensure_private_dir_exists('app-name')
    assert os.path.exists(private_dir.private_dir_path('app-name'))
    private_dir.ensure_private_dir_exists('app-name')
    assert os.path.exists(private_dir.private_dir_path('app-name'))


def test_ensure_private_dir_exists_conflict():
    assert not os.path.exists(private_dir.private_dir_path('app-name'))
    assert not os.system('touch {}'.format(private_dir.private_dir_path('app-name')))
    with pytest.raises(private_dir.PrivateDirConflictError):
        private_dir.ensure_private_dir_exists('app-name')

"""Tests for fileutils."""
import os
from unittest import TestCase

from recommendation_engine.utils.fileutils import *
from recommendation_engine.data_store.local_filesystem import LocalFileSystem

class TestFileUtils(TestCase):
    """Test the file utils module."""

    def test_save_temporary_local_file(self):
        """Test is able to save local temp file."""
        file_content = b"SomeContent"
        local_filename = 'test_fileutils_testfile.test.txt'
        save_temporary_local_file(file_content, local_filename)
        assert (os.stat(os.path.join('/tmp', local_filename)))

    def test_load_rating(self):
        file_system = LocalFileSystem('tests/test_data/')
        r = load_rating('test_load_rating.txt', file_system)
        self.assertListEqual(r, [{54909, 2309, 5409, 2054}, set()])

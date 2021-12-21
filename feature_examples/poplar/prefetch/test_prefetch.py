# Copyright (c) 2020 Graphcore Ltd. All rights reserved.
import os
import pytest

# NOTE: The import below is dependent on 'pytest.ini' in the root of
# the repository
from tutorials_tests.testing_util import SubProcessChecker

working_path = os.path.dirname(__file__)


class TestBuildAndRun(SubProcessChecker):

    def setUp(self):
        self.run_command("make", working_path, [])

    @pytest.mark.ipus(1)
    @pytest.mark.category1
    def test_run_prefetch(self):
        self.run_command("./prefetch",
                         working_path,
                         ["Running", "complete", "prefetch"])

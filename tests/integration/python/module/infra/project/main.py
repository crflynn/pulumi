# Copyright 2016-2020, Pulumi Corporation.  All rights reserved.

"""An example program that needs a venv to run"""

import pulumi

from infra.shared import shared_value
from infra import infra_value
from other import other_value

pulumi.export('foo', 'bar')

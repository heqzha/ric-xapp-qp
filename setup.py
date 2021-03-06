# ==================================================================================
#       Copyright (c) 2020 HCL Intellectual Property.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#          http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
# ==================================================================================

from setuptools import setup, find_packages

setup(
    name="qp",
    version="0.0.6",
    packages=find_packages(exclude=["tests.*", "tests"]),
    description="QoE prediction xApp that integrates with Traffic Steering",
    url="https://github.com/heqzha/ric-xapp-qp",
    install_requires=["ricxappframe>=2.0.0", "schedule>=1.1.0"],
    entry_points={"console_scripts": ["run-qp.py=qp.main:start"]},  # adds a magical entrypoint for Docker
    license="Apache 2.0",
    data_files=[("", ["LICENSE.txt"])],
)

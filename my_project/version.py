"""Version information for my_project."""

import packaging.version

version = "0.0.1"

package_version = packaging.version.parse(version)

__version__ = str(package_version)

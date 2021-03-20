import setuptools
import os
import glob

example_data = glob.glob('tabularasa/examples/*')
source_data = glob.glob('tabularasa/source/*')
test_data = glob.glob('tabularasa/test/*')
total_data = example_data + source_data + test_data
package_data = [x.replace('tabularasa/', '') for x in total_data]

#raise ValueError(f'PACKAGE DATA: {package_data}')

with open("README.md", "r") as fh:
	long_description = fh.read()

	setuptools.setup(
		name="tabularasa",
		version="0.1." + str(os.environ['GITHUB_RUN_NUMBER']),
		author="Jordan Edmunds",
		author_email="edmundsj@uci.edu",
		description="THIS IS A BRIEF DESCRIPTION",
		long_description=long_description,
		long_description_content_type="text/markdown",
		url="https://github.com/edmundsj/tabularasa",
		packages=setuptools.find_packages(),
		include_package_data=True,
		package_data={
			"tabularasa": package_data
			},
		classifiers=[
			"Programming Language :: Python :: 3",
			"License :: OSI Approved :: MIT License",
			"Operating System :: OS Independent",
		],
		python_requires='>=3.6',
		install_requires=[
				'numpy>=1.14.5',
				'matplotlib>=2.0.0',
				'pandas>=0.24.0',
				'scipy>=1.2.2',
				'pyyaml>=5.1.1',
                'pint>=0.16.0',
		],
	license="MIT",
	)

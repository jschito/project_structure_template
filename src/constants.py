#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Set of tools used in various modules"""

__author__ = 'XYZ'
__copyright__ = "Copyright 2021, YOUR_COMPANY"
__license__ = "BSD-3-Clause License"
__version__ = "0.0.1"
__status__ = "Development"


import os
import json


# ----- STRUCTURE DEFINITION
# Define important tables
src_dir = os.path.dirname(__file__)
root_dir = os.path.dirname(src_dir)
res_dir = os.path.join(root_dir, 'res')
output_dir = os.path.join(root_dir, 'output')

# Define important files
scenario_json = os.path.join(res_dir, 'scenario.json')


# ----- SCENARIO DEFINITION
# Import the scenario JSON
with open(scenario_json, encoding='utf8') as scenario_json_file:
    scenarios = json.load(scenario_json_file)


# ----- INITIALIZATION FUNCTION
# Define a function for initializing global variables passed by the main function
def init(*args):
    """
    This function loads all variables that depend on the location and set them as global variables.
    IMPORTANT: A valid configfile name must be provided! So please run configfile_information.CheckConfigFile() in
    advance.
    :param args: ONE string configfile name from all_configfiles.json containing the valid name of the config file
    :return: nothing
    """

    # Set, which scenario should be run. Remember that chosen_scenario is the scenario ending for the file name
    global chosen_scenario, at_least_one_student, scenario_with_student_numbers
    chosen_scenario = args[0]
    try:
        at_least_one_student = bool(scenarios['scenarios'][chosen_scenario]['at_least_one_student'])
        scenario_with_student_numbers = scenarios['scenarios'][chosen_scenario]['scenario_with_student_numbers']
    except KeyError as e:
        print('*** ERROR!!! You provided an argument that is not recorded in the JSON file. \n{}'.format(e))
        raise NotImplementedError


# ----- GLOBAL VARIABLES
# Initialize global variables
chosen_scenario = None
at_least_one_student = None
scenario_with_student_numbers = None

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Main function of your project. Describe it here."""

__author__ = 'XYZ'
__copyright__ = "Copyright 2021, YOUR_COMPANY"
__license__ = "BSD-3-Clause License"
__version__ = "0.0.1"
__status__ = "Development"

import os
import sys
import time
import pandas as pd
import helper
import constants as const


def main():
    """
    Main function
    :return:
    """

    # Create output dictionary
    # Headers: | scenario | one student | Betreuungsberufe | Detailhandelsberufe |
    assignment = []
    record = {
        'scenario': const.chosen_scenario,
        'one student': const.at_least_one_student,
        'Betreuungsberufe': const.scenarios['scenarios'][const.chosen_scenario]['berufsgattung']['Betreuungsberufe']['number'],
        'Detailhandelsberufe': const.scenarios['scenarios'][const.chosen_scenario]['berufsgattung']['Detailhandelsberufe']['number']
    }
    assignment.append(record)

    # Cast dictionary to dataframe, no matter if the result is infeasible or optimal
    # Sorted on Lehrgang first, Gemeinde second
    print('')
    print('Writing CSV file')
    assignment_df = pd.DataFrame.from_records(assignment)
    assignment_df.set_index(['scenario'], inplace=True)
    output_name = 'output_{}_{}'.format('scenario', const.chosen_scenario)
    helper.write_to_csv(assignment_df, output_name)


if __name__ == '__main__':
    # Initialize the current time
    time_0 = time.time()

    # Set the constants based on the defined config file (passed argument) and retrieve the argument dictionaries
    scenario_passed_as_argument = sys.argv[1]
    configfile_path = const.init(scenario_passed_as_argument)

    # Run the main function
    main()

    # Show the time needed to run the function
    print('')
    print('Whole process finished.')
    print('The process took {0:.2f} seconds.'.format(time.time() - time_0))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contains helper functions for optimizing global travel times across all students"""

__author__ = 'XYZ'
__copyright__ = "Copyright 2021, YOUR_COMPANY"
__license__ = "BSD-3-Clause License"
__version__ = "0.0.1"
__status__ = "Development"


import os
import errno
import constants as const


def ensure_directory_exists(directory):
    """
    Creates directory if it does not exist yet. If it exists if does nothing unless the error is something else.

    Parameters
    ----------
    directory : String
        Directory to be created
    """
    try:
        os.makedirs(directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


def get_file_directory(file):
    """
    Helper function to get the directory of a file.

    Parameters
    ----------
    file : String
        File to be searched for

    Returns
    ------
    file_path : String
        Path of the file
    """
    try:
        script_path = os.path.dirname(__file__)
    except NameError:
        return os.path.abspath(file)
    file_path = os.path.join(script_path, file)
    return file_path


def write_to_csv(output_df, output_name, output_dir='output'):
    """
    Helper function to export dataset to  CSV file.

    Parameters
    ----------
    output_df : pandas DataFrame
        Pandas Dataframe to be exported to CSV File. It should contain headers
    output_name : String
        Name of the output file, without file extension
    output_dir : String, optional
        Relative file path of the output file

    Returns
    -------
    None
    """
    ensure_directory_exists(const.output_dir)
    out_name = ''.join((output_name, '.csv'))
    output_df.to_csv(os.path.join(const.output_dir, out_name), encoding='latin-1', sep=';')

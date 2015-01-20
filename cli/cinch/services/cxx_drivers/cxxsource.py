#------------------------------------------------------------------------------#
# Copyright (c) 2014 Los Alamos National Security, LLC
# All rights reserved.
#------------------------------------------------------------------------------#

from string import Template

cxx_source_template = Template(
"""
/*--------------------------------------------------------------------------~~*
 * Copyright (c) 2014 Los Alamos National Security, LLC
 * All rights reserved.
 *--------------------------------------------------------------------------~~*/

#include <${FILENAME}>

/*
${TEMPLATE}void ${CLASSNAME}${TEMPLATE_TYPE}::method(argument_type & t)
{
} // ${CLASSNAME}${TEMPLATE_TYPE}::method

${TEMPLATE}void ${CLASSNAME}${TEMPLATE_TYPE}::method(argument_type & t)
{
} // ${CLASSNAME}${TEMPLATE_TYPE}::method
*/

/*-------------------------------------------------------------------------~--*
 * Formatting options for Emacs and vim.
 *
 * mode:c++
 * indent-tabs-mode:t
 * c-basic-offset:4
 * tab-width:4
 * vim: set tabstop=4 shiftwidth=4 expandtab :
 *-------------------------------------------------------------------------~--*/
""")

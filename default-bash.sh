#!/bin/bash
#
# This script is a default bash script with info error and debug msgs defined
#   A default usage and command line parser are provided

# Globals
GOOD_COLOR='\033[1;36m'
ERROR_COLOR='\033[1;31m'
DEBUG_COLOR='\033[1;32m'
WARN_COLOR='\033[1;33m'
NO_COLOR='\033[0m'
INFO_PREFIX="${GOOD_COLOR}INFO [%(%Y-%m-%dT%H:%M:%S%z)T]:"
ERROR_PREFIX="${ERROR_COLOR}ERROR [%(%Y-%m-%dT%H:%M:%S%z)T]:"
DEBUG_PREFIX="${DEBUG_COLOR}DEBUG [%(%Y-%m-%dT%H:%M:%S%z)T]:"
WARN_PREFIX="${WARN_COLOR}WARN [%(%Y-%m-%dT%H:%M:%S%z)T]:"

VERBOSITY=2

################################
# Prints usage 
# Globals:
#   None
# Arguments:
#   None
# Returns:
#   None
################################
default_print_usage() {
  printf "Usage: $0 [options]
    \t-h\t Display this help
    \t-v\t Set verbosity [0: silent, 1: info, 2: warn 3: debug] default 2
    "
  exit 0
}

################################
# Prints errors to stderr 
# Globals:
#   None
# Arguments:
#   Error message
# Returns:
#   None
################################
err() {
  printf "${ERROR_PREFIX} $@ ${NO_COLOR}\n" >&2
}

################################
# Prints information to stdout 
# Globals:
#   VERBOSITY
# Arguments:
#   Message
# Returns:
#   None
################################
info() {
  if [[ "${VERBOSITY}" -gt 0 ]]; then
    printf "${INFO_PREFIX} $@ ${NO_COLOR}\n"
  fi
}

################################
# Prints debug to stdout 
# Globals:
#   VERBOSITY
# Arguments:
#   Message
# Returns:
#   None
################################
debug() {
  if [[ "${VERBOSITY}" -gt 2 ]]; then
    printf "${DEBUG_PREFIX} $@ ${NO_COLOR}\n"
  fi
}

################################
# Prints warn to stdout 
# Globals:
#   VERBOSITY
# Arguments:
#   Message
# Returns:
#   None
################################
warn() {
  if [[ "${VERBOSITY}" -gt 1 ]]; then
    printf "${WARN_PREFIX} $@ ${NO_COLOR}\n"
  fi
}

################################
# Default command line parser
# Globals:
#   VERBOSITY
# Arguments:
#   $@
# Returns:
#   None
################################
default_cmd_line_parse() {
  while getopts ':v:' flag; do
    case "${flag}" in
      v) VERBOSITY="${OPTARG}" ;;
      *) default_print_usage ;;
    esac
  done
}

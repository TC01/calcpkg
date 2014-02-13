calcpkg 2.0 (in development) - ticalc.org Package Manager
=========================================================

calcpkg is a command line "package manager" for ticalc.org and other websites
with repositories of Texas Instruments calculator software.

What does that actually mean? Well, let's say you own a TI-83+ graphing calculator.
The 83+ can be programmed in a handful of languages, such as the builtin TI-BASIC
scripting language and z80 assembly. Using software such as TiLP, you can download
programs to your calculator to run them.

ticalc.org is the world's largest collection of TI graphing calculator software. It
features programs for every calculator model in almost every possible language, from
the ancient TI-81 to the newest models of TI-Nspire.

This program is a CLI interface to ticalc.org, allowing you to download programs
from the command line without having to browse the website in a web browser. It can
be configured to support other repositories as well.

Usage:
------

See INSTALL for install instructions.

The first command you should run is an update, to sync the index files:

`$ calcpkg update`

Then, you can search for files:

`$ calcpkg search [query]`

Then, the following command will download any files that match `[query]`:

`$ calcpkg install [query]`

You can narrow your search down with many flags. For instance, if you only want
to download TI-83+ games, you can use:

`$ calcpkg -g -c 83plus search [query]`

Then, if you want to automatically extract the downloaded .zip archives, you would
add the -x flag:

`$ calcpkg -x install [query]`

You can also simply count the number of files that match a given query:

`$ calcpkg count [query]`

For full documentation of all command line switches, run:

`$ calcpkg -h`

Legal Notes:
------------

This program is distributed under the MIT license, see LICENSE for details.

While ticalc.org staff members have okayed the use of this program to download
files from their website, this is not an endorsement of it- the program is
not written or maintained by them, it's written by me (see Credits).

Credits:
-------

-Ben 'TC01' Rosser <rosser.bjr@gmail.com>

Code or other technical assistance:
-Christopher "KermMartian" Mitchell
-Nathaniel "Eeems" van Diepen

-github .gitignore template

Help, feedback, etc. from:
-Travis "tev" Evans
-Kevin "DJ Omnimaga" Ouellat
-ephan (david, Scout, ScoutDavid)
-And other Cemetech and Omnimaga forum members

-ticalc.org staff

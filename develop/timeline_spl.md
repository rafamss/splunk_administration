# How to compare periods of time using appendcols and timewrap commands
**Created by:** Rafael Santos
**Version:** 1.0.0
**Splunk Version:** Above 7.x

1. Example 01 is using sub-querys to handle with the job
2. Example 02 is using the timewrap command to perform the same job
3. Both ways are correct. It's important to analyse which one will be better to do the work properly

#### Example 01
```
index=_internal sourcetype=splunkd log_level=error earliest=-0d@d latest=-0d@s 
| timechart count as Today 
| appendcols 
    [ search index=_internal sourcetype=splunkd log_level=error earliest=-1d@d latest=-1d@s 
    | timechart count as Yesterday ] 
| appendcols 
    [ search index=_internal sourcetype=splunkd log_level=error earliest=-1mon@d latest=-1mon@s 
    | timechart count as LastMonth ]
```

#### Example 02
```
index=main error
| timechart count span=1h
| timewrap d series=short
| addtotals s*
| eval 7dayavg=Total/7.0
| table _time, _span, s0, s1, 7dayavg
| rename s0 as now, s1 as yesterday
```
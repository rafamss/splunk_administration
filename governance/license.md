* **To analysis the amount in GB of the use of License by Index and Sourcetype**
    * **To better performance, it's important to schedule a report or summarize the data.**

```
index=_internal source=*license_usage.log type="Usage" 
| eval indexname = if(len(idx)=0 OR isnull(idx),"(UNKNOWN)",idx)
| eval sourcetypename = st
| bin _time span=1d 
| stats sum(b) as b by _time, pool, indexname, sourcetypename
| eval GB=round(b/1024/1024/1024, 3)
| fields _time, indexname, sourcetypename, GB
```

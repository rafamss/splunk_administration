There are three ways to verify the ports that are configured for Splunk. By default, Splunk will run on port 8000 for the web services and port 8089 for splunkd services. 

Check the $SPLUNK_HOME/etc/system/local/web.conf for port settings: 

mgmtHostPort = 127.0.0.1:8089 
httpport = 8000 

Run the following command: 

```
./splunk show web-port 
./splunk show splunkd-port
```

Use the btool command to see web.conf settings: 
```
./splunk cmd btool web list --debug
```

## Check the size of indexes showing the size in MB and GB ##

```| REST /services/data/indexes 
| eval currentDBSizeGB=round((currentDBSizeMB/1024), 2) 
| table splunk_server, title, currentDBSizeMB, currentDBSizeGB 
| sort - currentDBSizeGB
```

## Check the minimum and maximum date and time of storage data of indexes ##

```
| metadata index=index* type=sourcetypes 
| eval it=strftime(firstTime,"%Y-%m-%d %H:%M:%S")
| eval et=strftime(lastTime,"%Y-%m-%d %H:%M:%S")
| stats min(it) AS DataInitial, max(et) AS DataFinal by sourcetype
```

## See the data receiving by forwarder type ##

```
index=_internal source=*metrics.log group=tcpin_connections 
| stats values(sourceIp) count by fwdType
```

## How to determine my indexing volume by host, source, or sourcetype ##

-> Per host:
```
index="_internal" source="*metrics.log" group="per_host_thruput" | chart sum(kb) by series | sort - sum(kb)
```
-> Per source:
```
index="_internal" source="*metrics.log" group="per_source_thruput" | chart sum(kb) by series | sort - sum(kb)
```
-> Per sourcetype:
```
index="_internal" source="*metrics.log" group="per_sourcetype_thruput" | chart sum(kb) by series | sort - sum(kb)
```
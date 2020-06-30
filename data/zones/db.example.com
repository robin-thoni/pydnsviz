$ORIGIN .
$TTL 86400	; 1 day
example.com	IN SOA	ns1.example.com. hostmaster.example.com. (
				2002022402 ; serial
				10800      ; refresh (3 hours)
				15         ; retry (15 seconds)
				604800     ; expire (1 week)
				10800      ; minimum (3 hours)
				)
$TTL 600	; 10 minutes
			NS	ns1.example.com.
			NS	ns2.example.com.
$ORIGIN example.com.
$TTL 600	; 10 minutes
ns1 			A   	42.42.42.10
ns2 			A   	42.42.42.11

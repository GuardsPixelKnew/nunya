#SSH default files and settings

#SSHD:
#/etc/ssh/sshd_config
	#/usr/sbin/sshd -f <alternate.config>
	#/usr/sbin/sshd -f <alternate.config> -p <alternate port>
	#/usr/sbin/sshd -d #debug

#UseDNS - setting this to yes will enable the checking of
#connections with DNS but will also generate traffic with third parties
#identifying end points. ...which is kind of the purpose.
USE_DNS_SETTING='UseDNS yes'
SYSLOG_SETTING='SyslogFacility AUTH'
log_levels=['INFO', 'QUIET', 'FATAL', 'ERROR', 'INFO',
 'VERBOSE', 'DEBUG1', 'DEBUG2', 'DEBUG3']
LOG_LEVEL_SETTING='LogLevel ' #add a log_levels setting
PASSWORD_AUTH_SETTING='PasswordAuthentication no'
X11FORWARD_SETTING='X11Forwarding no'
STRICT_HOSTKEY_CHECK_SETTING='StrictHostKeyChecking yes'
HASH_KNOWN_HOSTS_SETTING='HashKnownHosts yes'
CHALLENGE_RESPONSE_AUTH_SETTING='ChallengeResponseAuthentication no'
PUBKEY_AUTH_SETTING='PubkeyAuthentication yes'
TCP_KEEP_ALIVE_SETTING='TCPKeepAlive yes'
GATEWAY_PORTS_SETTINGS='GatewayPorts no'

default_settings=[USE_DNS_SETTING, SYSLOG_SETTING, LOG_LEVEL_SETTING,
PASSWORD_AUTH_SETTING, X11FORWARD_SETTING, STRICT_HOSTKEY_CHECK_SETTING,
HASH_KNOWN_HOSTS_SETTING, CHALLENGE_RESPONSE_AUTH_SETTING,
PUBKEY_AUTH_SETTING, TCP_KEEP_ALIVE_SETTING, GATEWAY_PORTS_SETTINGS,
]

#SSH:


#SSH PATHES:
BASE_PATH='/etc/ssh'
CLIENT_FILE='ssh_config'
HOST_FILE='sshd_config'
#I am not supporting protocol version 1
#So I am not providing default variables
#for its configuration.
HOSTKEY_PRIVATE_RSA='ssh_host_rsa_key'
HOSTKEY_PRIVATE_DSA='ssh_host_dsa_key'
HOSTKEY_PRIVATE_ECDSA='ssh_host_ecdsa_key'
HOSTKEY_PUBLIC_RSA='ssh_host_rsa_key.pub'

#REGEXP for common config file changes:
#The grouping is used to make it easy to append or 
#copy the current configuration.

PORT='(^[Pp]ort\s)(*$)'
#Address family options are inet inet6
ADDRESS_FAMILY='(^[Aa]ddress[Ff]amily)(*$)'
# There may be multiple listening addresses
LISTEN_ADDRESS='^[Ll}isten[Aa]ddress(*$)'
USE_DNS='(^[Uu]se[Dd][Nn][Ss])(*$)'
SYSLOG='(^[Ss]log[Ff]acility)(*$)'
LOG_LEVEL='(^[Ll]og[Ll]evel)(*$)'
#Users can be referred to by name or also by
#name and origin - example: user@192.0.2.0/25
#Wild cards can also be used.
ALLOW_USERS='(^[Aa]llow[Uu]sers)(*$)'
DENY_USERS='(^[Dd]eny[Uu]sers(*$)'
ALLOW_GROUPS='(^[Aa]llow[Gg]roups)(*$)'
DENY_GROUPS='(^[Dd]eny[Gg]roups)(*$)'
MATCH_ADDRESS='(^[Mm]atch\s[Aa]ddress)(*$)'
MATCH_HOST='(^[Mm]atch\s[Hh]ost)(*$)'
PASSWORD_AUTH='(^[Pp]assword[Aa]uthentication)(*$)'
CHROOT_DIR='(^[Cc]root[Dd]irectory)(*$)'
HOST='[Hh]ost)(*$)'
FORWARD_AGENT='([Ff]orward[Aa]gent)(*$)'
FORWARD_X11='([Ff]orward[Xx]11)(*$)'
FORWARD_X11_TRUSTED='([Ff]orward[Xx]11[Tt]rusted)(*$)'
RHOST_RSA_AUTH='([Rr]hosts[R][Ss][Aa][Aa]uthentication)(*$)'
RSA_AUTH='([Rr][Ss][Aa][Aa]uthentication)(*$)'
HOSTBASED_AUTH='([Hh]ostbased[Aa]uthentication)(*$)'
GSSAPI_AUTH='([Gg][Ss][Ss][Aa][Pp][Ii][Aa]uthentication)(*$)'
GSSAPI_DELEGATE_CREDENTIALS='([Gg][Ss][Ss][Aa][Pp][Ii][Dd]elegate[Cc]redentials)(*$)'
GSSAPI_KEY_EXCHANGE='([Gg][Ss][Ss][Aa][Pp][Ii][K]ey[E]xchange)(*$)'
GSSAPI_TRUST_DNS='([Gg][Ss][Ss][Aa][Pp][Ii][T]rust[D]NS)(*$)'
MATCH_MODE='([Bb]atch[Mm]ode)(*$)'
CHECK_HOST_IP='([Cc]heck[Hh]ost[Ii]Pp)(*$)'
CONNECT_TIMEOUT='([Cc]onnect[Tt]imeout)(*$)'
STRICT_HOSTKEY_CHECK='([Ss]trict[Hh]ost[Kk]ey[Cc]hecking)(*$)'
ID_FILE='([Ii]dentity[Ff]ile)(*$)'
PROTOCOL='([Pp]rotocol)(*$)'
CIPHER='([Cc]ipher)(*$)'
CIPHERS='([Cc]iphers)(*$)'
MACS='([Mm][Aa][Cc]s)(*$)'
ESC_CHAR='([Ee]scape[Cc]har)(*$)'
TUNNEL='([Tt]unnel)(*$)'
TUNNEL_DEVICES='([Tt]unnel[Dd]evice)(*$)'
PERMIT_LOCAL_COMMAND='([Pp]ermit[Ll]ocal[Cc]ommand)(*$)'
VISUAL_HOSTKEY='([Vv]isual[Hh]ost[Kk]ey)(*$)'
PROXY_COMMAND='([Pp]roxy[Cc]ommand)(*$)'
SEND_ENV='([Ss]end[Ee]nv)(*$)'
HASH_KNOWN_HOSTS='([Hh]ash[Kk]nown[Hh]osts)(*$)'
ALLOW_TCP_FORWARDING='(^[Aa]llow[Tt]cp[Ff]orwarding)(*$)'
SUBSYSTEM='(^[Ss]ubsystem)(*$)'
CHALLENGE_RESPONSE_AUTH='(^[Cc]allenge[Rr]esponse[Aa]uthentication)(*$)'
PUBKEY_AUTH='(^[Pp]ubkey[Aa]uthentication)(*$)'
LOCAL_FORWARD='(^[Ll]ocal[Ff]orward)(*$)'
REMOTE_FORWARD='(^[Rr]emote[Ff]orward)(*$)'
DYNAMIC_FORWARD='(^[Dd]ynamic[Ff]orward)(*$)'
PRINT_MOTD='(^[Pp]rint[Mm]otd)(*$)'
X11_DISPLAY_OFFSET='(^[Xx]11[Dd]isplay[Oo]ffset)(*$)'
TCP_KEEP_ALIVE='(^[Tt][Cc][Pp][Kk]eep[Aa]live)(*$)'
GATEWAY_PORTS='(^[Gg]ateway[Pp]orts)(*$)'
CLIENT_ALIVE_INTERVAL='(^[Cc]lient[Aa]live[Ii]nterval)(*$)'
CLIENT_ALIVE_MAX='(^[Cc]lient[Aa]live[Mm]ax)(*$)'

config_options=[PORT, ADDRESS_FAMILY, LISTEN_ADDRESS, USE_DNS, 
SYSLOG, LOG_LEVEL, ALLOW_USERS,DENY_USERS, MATCH_ADDRESS, MATCH_HOST,
PASSWORD_AUTH, CHROOT_DIR, HOST, FORWARD_AGENT, FORWARD_X11,
FORWARD_X11_TRUSTED, RHOST_RSA_AUTH, RSA_AUTH, HOSTBASED_AUTH, GSSAPI_AUTH,
GSSAPI_DELEGATE_CREDENTIALS, GSSAPI_KEY_EXCHANGE, GSSAPI_TRUST_DNS,
MATCH_MODE, CHECK_HOST_IP, CONNECT_TIMEOUT, STRICT_HOSTKEY_CHECK, ID_FILE,
PROTOCOL, CIPHER, CIPHERS, MACS, ESC_CHAR, TUNNEL, TUNNEL_DEVICES, 
PERMIT_LOCAL_COMMAND, VISUAL_HOSTKEY, PROXY_COMMAND, SEND_ENV, 
HASH_KNOWN_HOSTS, ALLOW_TCP_FORWARDING, SUBSYSTEM, CHALLENGE_RESPONSE_AUTH,
LOCAL_FORWARD, REMOTE_FORWARD, DYNAMIC_FORWARD, PRINT_MOTD, X11_DISPLAY_OFFSET,
TCP_KEEP_ALIVE, GATEWAY_PORTS, CLIENT_ALIVE_INTERVAL, CLIENT_ALIVE_MAX, 
]
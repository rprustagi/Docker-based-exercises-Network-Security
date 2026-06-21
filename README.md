# Docker-Based Exercises for Computer Networks and Security
Here you will find docker compose files to implement various exercises related to Computer Network and Security. These exercises enables any learner to use the experiential learning, i.e., learn by doing it, to understand the key concepts in network and security

All the docker compose files have extension .yml.

These exercises can be carried out under Docker desktop of Windows, Macbook. Also, these can be carried out in Ubuntu (or any other Linux) based system.


This repository contains Docker-based laboratory exercises for teaching and learning Computer Networks and Network Security. The exercises are designed for experiential learning: students build a topology, run commands, observe packet behavior, and explain the result.

The repository is organized around two main directories:

```text
df/     Dockerfiles and supporting files copied into Docker images
yml/    Docker Compose files for individual lab topologies
```

The Compose files can be used on Docker Desktop for Windows/macOS and on Linux systems.

---

## Quick Start

Clone the repository:

```bash
git clone https://github.com/rprustagi/Docker-based-exercises-Network-Security.git
cd Docker-based-exercises-Network-Security
```

Run a lab:

```bash
cd yml
docker compose -f <compose-file.yml> up --build
```

Stop and clean up a lab:

```bash
docker compose -f <compose-file.yml> down
```

Remove containers, networks, and volumes when needed:

```bash
docker compose -f <compose-file.yml> down -v
```

---

## Suggested Learning Approach

For each exercise, students should follow the following cycle:

1. **Predict** — Before running the lab, predict what should happen.
2. **Implement** — Start the Docker topology and configure hosts/routers/firewalls.
3. **Observe** — Use tools such as `ping`, `ip route`, `tcpdump`, `traceroute`, `curl`, `dig`, `nc`, and Wireshark.
4. **Explain** — Explain the observed behavior using protocol concepts.

---

## Directory Overview

| Directory | Purpose |
|---|---|
| `df/` | Dockerfiles for base host, router, firewall, web, Kerberos, PostgreSQL, TCP echo, websocket, and load balancer images. |
| `df/Programs/` | Python, shell, HTML, CSS, and packet manipulation programs used by multiple labs. |
| `df/Scripts/` | Initialization and setup scripts copied into containers. |
| `df/bin/` | Startup scripts used by selected images. |
| `df/cgi-bin/` | CGI examples for web security and server-side scripting demonstrations. |
| `df/clickjack/` | Clickjacking, iframe, CSP, and X-Frame-Options demo pages. |
| `df/conf/` | Apache, Nginx, Kerberos, and SSH configuration files. |
| `df/html/` | Static and dynamic web content for web, XSS, CSRF, cookie, JavaScript, and websocket labs. |
| `yml/` | Docker Compose topologies for LANs, routers, firewall, ICMP, IPv6, VLAN, websocket, load balancing, and other exercises. |

---

# `df/`: Dockerfiles and Image Definitions

The `df/` directory contains Dockerfiles used to build reusable images for the exercises.

| File | Brief Description | Typical Use |
|---|---|---|
| `hello.df` | Iintroductory Dockerfile. | Simple Docker image build for environment test. |
| `krb-client.df` | Kerberos Client image. | Kerberos authentication; runs tools such as `kinit`, `kvno`, and SSH client. |
| `krb-kdc.df` | Kerberos Key Distribution Center image. | KDC/admin server for Kerberos realm experiments. |
| `krb-server.df` | Kerberos SSH server image. | SSH/GSSAPI or service-principal authentication labs. |
| `nginx-lb.df` | Nginx-based load balancer image. | HTTP load balancing and reverse proxy exercises. |
| `postgres.df` | PostgreSQL database image. | SQL and database connectivity exercises. |
| `tcp-echo-server.df` | TCP echo server image. | Socket programming and TCP client/server labs. |
| `ub22-clickjack.df` | Ubuntu 22 based image for clickjacking/web-security labs. | Clickjacking, CSP, iframe, X-Frame-Options demos. |
| `ub22-host-fw.df` | Ubuntu 22 host/firewall image. | Firewall, iptables/nftables, host security labs. |
| `ub22-websocket.df` | Ubuntu 22 websocket/web server image. | WebSocket chat, web security, and JavaScript-based demos. |
| `ubuntu-host.df` | General Ubuntu host image |  End hosts in most networking and security exercises. |
| `ubuntu-router.df` | General Ubuntu router image | Router containers in  networking and security exercises. |

---

# `df/Programs/`: Program Files

The `df/Programs/` directory contains Python scripts, shell scripts, and web files used inside the lab containers.

## Web/HTML/CSS Files

| File | Brief Description |
|---|---|
| `Description-builtin-style.html` | HTML example with inline CSS styling. |
| `Description-external-css.html` | HTML example using external CSS. |
| `style-dscr.css` | A Sample CSS file  |

## ARP, Spoofing, Sniffing, and Packet Manipulation

| File | Brief Description |
|---|---|
| `arp_spoof.sh` | Shell script for ARP spoofing demonstration. |
| `arp_spoof_param.py` | Parameterized ARP spoofing script. |
| `fragment_spoof_udp.py` | UDP packet spoofing with fragmentation. |
| `fragment_spoof_udp_overlap.py` | UDP fragmentation overlap demonstration. |
| `sniff_display.py` | Packet sniffer that displays captured packet details. |
| `sniff_simple.py` | Simple packet sniffer. |
| `sniff_spoof_icmp.py` | ICMP sniffing/spoofing demonstration. |
| `spoof_icmp.py` | ICMP packet spoofing script. |
| `spoof_icmp_redirect.py` | ICMP redirect spoofing script. |
| `spoof_mac_udp.py` | UDP spoofing with MAC address manipulation. |
| `spoof_udp.py` | UDP spoofing demonstration. |

## TCP Programs and Attacks

| File | Brief Description |
|---|---|
| `mitm_tcp.py` | TCP man-in-the-middle demonstration script. |
| `mitm_tcp_nc.py` | TCP MITM variation using netcat-style communication. |
| `tcp_FIN.py` | TCP FIN/connection-closing experiment. |
| `tcp_client-1msg.py` | TCP client that sends one message. |
| `tcp_client-3msgs.py` | TCP client that sends three messages. |
| `tcp_client.py` | General TCP client. |
| `tcp_client_half_close.py` | TCP client demonstrating half-close behavior. |
| `tcp_echo_server.py` | TCP echo server. |
| `tcp_hijack.py` | TCP session hijacking demonstration. |
| `tcp_reset.py` | TCP reset attack demonstration. |
| `tcp_server-1client-loop.py` | TCP server loop for a single client. |
| `tcp_server.py` | General TCP server. |
| `tcp_server_1msg.py` | TCP server for one-message exchange. |
| `tcp_server_half_close.py` | TCP server demonstrating half-close behavior. |
| `tcp_server_preforked.py` | Preforked TCP server. |
| `tcp_server_process_spawn.py` | TCP server that spawns a process per connection. |
| `tcp_server_select.py` | TCP server using `select()`. |
| `tcp_server_socket.py` | Basic TCP socket server. |
| `tcp_syn_flooding.py` | TCP SYN flooding demonstration. |

## UDP Programs

| File | Brief Description |
|---|---|
| `mitm_udp_nc.py` | UDP MITM variation using netcat-style communication. |
| `reorder_drop.py` | Packet reordering/drop experiment. |
| `udp_client.py` | General UDP client. |
| `udp_client_flooding.py` | UDP flooding client. |
| `udp_random_delay.py` | UDP delay variation experiment. |
| `udp_reorder.py` | UDP packet reordering demonstration. |
| `udp_server.py` | General UDP server. |
| `udp_server_echo.py` | UDP echo server. |

## WebSocket and SOCKS/Tunnel Programs

| File | Brief Description |
|---|---|
| `chat_websocket_server.py` | WebSocket chat server. |
| `demo-ws.py` | WebSocket demonstration program. |
| `socks_nc_client.py` | SOCKS/netcat-style client. |
| `socks_web_client.py` | SOCKS/web client demonstration. |
| `tun0.py`, `tun1.py`, `tun2.py` | TUN interface examples. |
| `tun_client.py` | Tunnel client program. |
| `tun_server.py` | Tunnel server program. |

## VLAN Helper Scripts

| File | Brief Description |
|---|---|
| `vlan0-create-interfaces.sh` | Creates base interfaces for VLAN lab. |
| `vlan1-create-bridge-if-inside-switch.sh` | Creates bridge/interface structure inside switch containers. |
| `vlan2-create-vlans.sh` | Creates VLAN interfaces. |
| `vlan3-assign-ips.sh` | Assigns IP addresses for VLAN exercises. |

---

# `df/Scripts/`: Container Setup Scripts

| File | Brief Description |
|---|---|
| `create-interface.sh` | Creates or configures network interfaces. |
| `create-interfaces.h` | Header/helper file for interface creation. Verify extension/name. |
| `krb-kdc-init.sh` | Initializes Kerberos KDC services, principals, or realm data. |
| `krb-server-init.sh` | Initializes Kerberos server configuration and keytabs. |
| `vlans-create-bridge-if-inside-switch.sh` | Creates bridge interfaces inside VLAN switch containers. |
| `vlans-create-vlans.sh` | Creates VLAN interfaces for VLAN lab. |

---

# `df/bin/`: Startup Helpers

| File | Brief Description |
|---|---|
| `start.sh` | Startup script used by selected Docker images. |

---

# `df/cgi-bin/`: CGI Examples

| File | Brief Description |
|---|---|
| `badcgi.cgi` | CGI script intentionally demonstrating unsafe/bad CGI behavior. |
| `badcgi.py` | Python version of bad CGI example. |
| `cookiex.py` | Cookie-related CGI example. |
| `goodcgi.cgi` | Safer CGI example. |
| `goodcgi.py` | Python version of safer CGI example. |
| `index.cgi` | CGI index/entry script. |

---

# `df/clickjack/`: Clickjacking, CSP, and X-Frame-Options Demo Files

| File | Brief Description |
|---|---|
| `buttonwithlike.html` | Button/like page used in clickjacking demonstration. |
| `csp-all.php` | CSP demo allowing broader content policy. |
| `csp-demo.html` | Content Security Policy demo page. |
| `csp-self.php` | CSP demo using `self`. |
| `csp-url.php` | CSP demo using a specific URL. |
| `iframeiniframe.html` | Nested iframe demonstration. |
| `iframesbasic.html` | Basic iframe example. |
| `iframesopacity.html` | Iframe opacity-based clickjacking demo. |
| `iframesoverlap.html` | Overlapping iframe demo. |
| `likebuttonunlikesmall.html` | Like/unlike button clickjacking variant. |
| `likes.html` | Like button demo page. |
| `likes1.html` | Alternate like page. |
| `likespng.html` | Like demo using PNG asset. |
| `likesunlikesoverlap.html` | Overlap demo using like/unlike elements. |
| `likeunlike0.html` | Like/unlike demo variant 0. |
| `likeunlike1.html` | Like/unlike demo variant 1. |
| `likeunlike2.html` | Like/unlike demo variant 2. |
| `likeunlikesmall.html` | Small like/unlike demo. |
| `smallunlike.html` | Small unlike demo. |
| `unlikes.html` | Unlike button demo page. |
| `unlikes1.html` | Alternate unlike page. |
| `unlikespng.html` | Unlike demo using PNG asset. |
| `xframe-deny.php` | X-Frame-Options DENY example. |
| `xframe-none.php` | Example page without X-Frame-Options protection. |
| `xframe-options.html` | X-Frame-Options explanation/demo page. |
| `xframe-sameorigin.php` | X-Frame-Options SAMEORIGIN example. |
| `brown.jpeg`, `green.jpeg` | Image assets for clickjacking pages. |
| `likes.png`, `likes2.png`, `olikes.png` | Like button image assets. |
| `ounlikes.png`, `unlikes.png` | Unlike button image assets. |

---

# `df/conf/`: Configuration Files

| File | Brief Description |
|---|---|
| `000-default.conf` | Apache default virtual host configuration. |
| `000-proxy.conf` | Apache proxy/reverse proxy configuration. |
| `client-krb5.conf` | Kerberos client configuration. |
| `kdc-kadm5.acl` | Kerberos admin ACL configuration. |
| `kdc-krb5.conf` | Kerberos configuration for KDC. |
| `kdc.conf` | KDC service configuration. |
| `nginx_lb_echo.conf` | Nginx load balancing configuration for echo service. |
| `nginx_lb_web.conf` | Nginx load balancing configuration for web service. |
| `nginx_lb_web_echo.conf` | Nginx load balancing configuration for combined web/echo service. |
| `server-krb5.conf` | Kerberos server-side configuration. |
| `server-sshd_config` | SSH daemon configuration for Kerberos/GSSAPI server. |

---

# `df/html/`: Web Content

| Path/File | Brief Description |
|---|---|
| `cookies/` | Cookie demonstration pages. |
| `csrf/` | Cross-Site Request Forgery lab pages. |
| `css/` | CSS files used by web labs. |
| `forms/` | HTML form examples. |
| `img/` | Image assets for web labs. |
| `js/` | JavaScript files used by web labs. |
| `mixed/` | Mixed content or mixed web demo files. |
| `private/` | Private/protected content examples. |
| `websocket/` | WebSocket client pages and related content. |
| `xss/` | Cross-Site Scripting lab pages. |
| `example.php` | PHP example page. |
| `examplejs.html` | JavaScript example page. |
| `noperm.html` | Permission/access-control demonstration page. |
| `pictures.html` | HTML page displaying images. |
| `pictures.txt` | Text companion file for pictures demo. |
| `welcome.html` | Welcome page. |
| `welcome.txt` | Text companion welcome file. |

---

# `df/TBD/`: Work-in-Progress Dockerfiles

| File | Brief Description |
|---|---|
| `arm64-ub22-mailserver.df` | ARM64 Ubuntu 22 mail server Dockerfile; likely used for SMTP/IMAP/POP3 mail labs. |
| `arm64-ub22-webmail.df` | ARM64 Ubuntu 22 webmail Dockerfile; likely used for Roundcube/webmail labs. |

---

# `yml/`: Docker Compose Lab Files

The `yml/` directory contains Docker Compose files. Each file defines a complete lab topology.

| Compose File | Brief Description | Main Concepts |
|---|---|---|
| `FW-3H3S1N.yml` | Firewall topology with three hosts, three servers, and one network/firewall node. | Firewall rules, filtering, NAT, host/server access control. |
| `LAN-2R2H.yml` | LAN topology with two routers and two hosts. | Static routing, forwarding, multi-hop connectivity. |
| `LAN-2R3H.yml` | LAN topology with two routers and three hosts. | Multi-host routing and reachability testing. |
| `LAN-2R4H.yml` | LAN topology with two routers and four hosts. | Routing, subnetting, path verification. |
| `LAN-3R2H.yml` | LAN topology with three routers and two hosts. | Multi-router forwarding, route setup, traceroute analysis. |
| `LAN-4H.yml` | Simple LAN with four hosts. | Same-subnet communication, ARP, broadcast behavior. |
| `LAN6-2R2H.yml` | IPv6-only or IPv6-focused topology with two routers and two hosts. | IPv6 addressing, routing, ICMPv6. |
| `LAN64-2R2H.yml` | Dual-stack IPv6/IPv4 topology with two routers and two hosts. | IPv4 + IPv6 coexistence. |
| `LAN64-3R2H-v6-over-v4.yml` | IPv6-over-IPv4 tunneling topology with three routers and two hosts. | IPv6 tunneling over IPv4, protocol 41, dual stack. |
| `LB-web-echo.yml` | Load balancing topology for web and echo services. | Nginx load balancing, backend services, HTTP/TCP testing. |
| `LPM-Routing.yml` | Longest Prefix Match routing topology. | Overlapping prefixes, route specificity, forwarding decisions. |
| `Routing-Loop.yml` | Routing loop topology. | Default routes, loops, TTL expiration, ICMP Time Exceeded. |
| `clickjack.yml` | Clickjacking/web-security topology. | Iframes, clickjacking, CSP, X-Frame-Options. |
| `icmp-PMTU.yml` | ICMP Path MTU Discovery topology. | MTU, fragmentation, ICMP “fragmentation needed”. |
| `icmp-redirect-analyse.yml` | ICMP Redirect analysis topology. | Legitimate ICMP redirects, route optimization, packet analysis. |
| `icmp-redirect-attack.yml` | ICMP Redirect attack topology. | Malicious redirect, MITM, routing manipulation. |
| `sql-postgres.yml` | PostgreSQL database lab topology. | Database server, client access, SQL practice. |
| `udp-loss-reorder.yml` | UDP loss/reordering topology. | UDP unreliability, packet loss, reordering, delay. |
| `vlans.yml` | VLAN topology. | VLAN isolation, trunking, inter-VLAN routing. |
| `websocket.yml` | WebSocket lab topology. | WebSocket chat, browser clients, JavaScript/network security. |

## Nginx Configuration Files in `yml/`

| File | Brief Description |
|---|---|
| `nginx_lb_echo.conf` | Nginx configuration for load balancing echo-style backend services. |
| `nginx_lb_web.conf` | Nginx configuration for HTTP web backend load balancing. |
| `nginx_lb_web_echo.conf` | Nginx configuration for combined web and echo service load balancing. |

---

##  Documentation  for Each Lab

For every Compose file,  a short section on its usage (TBD)

```markdown
## Lab: <compose-file-name>

### Purpose
Briefly describe what this lab demonstrates.

### Topology
List hosts, routers, servers, firewalls, and Docker networks.

### Main Concepts
- Concept 1
- Concept 2
- Concept 3

### How to Run
```bash
docker compose -f <compose-file-name> up --build
```

### Basic Verification
```bash
docker exec -it <container> bash
ip addr
ip route
ping <target-ip>
tcpdump -i any -n
```

### Suggested Methodology for Experiential Learning exercises
1. Predict what should happen.
2. Run the commands.
3. Observe packets using tcpdump/Wireshark.
4. Explain the observed behavior.

### Cleanup
```bash
docker compose -f <compose-file-name> down -v
```
```

---

## Common Commands

Enter a container:

```bash
docker exec -it <container-name> bash
```

List containers:

```bash
docker ps
```

Show IP addresses:

```bash
ip addr
```

Show routes:

```bash
ip route
ip -6 route
```

Capture packets:

```bash
tcpdump -i any -n
tcpdump -i any -nn -e
tcpdump -i any -n icmp
tcpdump -i any -n tcp
tcpdump -i any -n udp
```

Test HTTP:

```bash
curl http://<server-ip>
```

Test DNS:

```bash
dig @<dns-server-ip> <name>
```

Test TCP/UDP with netcat:

```bash
nc -l -p 5000
nc <server-ip> 5000

nc -u -l -p 6000
nc -u <server-ip> 6000
```

---

##  README Improvements (TBD)

- Add one paragraph for each Compose file explaining its learning goal.
- Add a topology diagram or ASCII diagram for each major lab.
- Add a table of container names and IP addresses for every lab.
- Add expected `ping`, `traceroute`, `curl`, `dig`, or `tcpdump` output.
- Mark labs as Beginner, Intermediate, or Advanced.
- Mention whether the lab requires Linux-specific privileges, Docker Desktop, or Apple Silicon changes.
- Add cleanup commands for each exercise.
- Add a troubleshooting section for common Docker/networking issues.

---

## Troubleshooting Notes

### Docker Compose Build Fails

Try:

```bash
docker compose -f <file.yml> build --no-cache
```

### Containers Start but Cannot Ping

Check:

```bash
ip addr
ip route
sysctl net.ipv4.ip_forward
```

For router containers, ensure IP forwarding is enabled.

### Docker Networks Persist After Cleanup

Use:

```bash
docker network ls
docker compose -f <file.yml> down -v
```

### Need Packet Visibility

Use:

```bash
tcpdump -i any -nn -e
```

Use `-e` when Ethernet/VLAN headers are important.

---

## License

This repository is licensed under the Apache-2.0 License. See `LICENSE` for details.

---

## Maintainer Notes

This README is intended as a basic help and overview on usage of docker files. Real learning will occur with actual network creation, implementation of exercises, observation of network behaviour and explanation of the behaviour.

FROM ubuntu:22.04

RUN apt-get update && apt-get install -y openssh-server sudo && rm -rf /var/lib/apt/lists/*

RUN useradd -m -s /bin/bash lowpriv && echo "lowpriv:password123" | chpasswd

RUN mkdir /var/run/sshd

RUN echo "NEXORA{r00t_4cc3ss_gr4nt3d}" > /root/flag.txt && chmod 600 /root/flag.txt

RUN chmod u+s /usr/bin/find

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]

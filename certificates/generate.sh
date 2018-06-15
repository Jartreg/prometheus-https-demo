#!/bin/sh

. ./config.sh

function createCA {
	openssl req -x509 -new -nodes -newkey rsa:4096 -sha256 -keyout "$1-authority.key.pem" -out "$1-authority.cert.pem" -utf8 -subj "/CN=$2/C=DE"
}

function createCSR {
	openssl req -nodes -newkey rsa:2048 -sha256 -keyout "$1.key.pem" -out "$1.csr" -utf8 -subj "/CN=$2/C=DE"
}

function createCert {
	openssl x509 -req -in "$1.csr" -CA "$1-authority.cert.pem" -CAkey "$1-authority.key.pem" -CAcreateserial -out "$1.cert.pem" -sha256 -extfile ../site.ext
}

function cleanup {
	rm "$1.csr"
	rm "$1-authority.key.pem"
	rm "$1-authority.srl"
}

function createExtFile {
	echo "authorityKeyIdentifier=keyid,issuer
basicConstraints=CA:FALSE
keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment
subjectAltName = @alt_names

[alt_names]
DNS.1 = $SITE_ADDRESS" > site.ext
}

function createProxyCert {
	cat $1-authority.key.pem > mitmproxy-ca.pem
	cat $1-authority.cert.pem >> mitmproxy-ca.pem
}

function createCertificates {
	mkdir $1
	cd $1
	createCA $1 "$2"
	createCSR $1 "$SITE_NAME"
	createCert $1

	if [ "$1" == 'attacker' ]; then
		createProxyCert $1
	fi

	cleanup $1
}

createExtFile
createCertificates site "$SITE_CA_NAME" &
createCertificates attacker "$ATTACKER_CA_NAME" &

wait
rm site.ext

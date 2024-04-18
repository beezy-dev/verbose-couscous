package main

import (
	"flag"
	"fmt"
	"log"
	"net/http"
	"os"
	"time"
)

func main() {

	var (
		listenAddr   = flag.String("listen-addr", "0.0.0.0:8080", "Service IP and Port with default 0.0.0.0:8080")
		mySecret     = flag.String("mysecret", "1234", "Default secret is 1234")
		reloadEnable = flag.Bool("reload", false, "Enable the configuration reload capability.")
	)

	flag.Parse()

	// Intanciate a custom logger by function.
	hplog := log.New(os.Stdout, "[hello-path-go-main] ", log.LstdFlags)

	// Define a handler for pseudo GET requests.
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		path := r.URL.Path

		// conditional message based on the provided path.
		if path == "/mysecret" {
			// return value to the pseudo GET request
			fmt.Fprintf(w, "my little secret is %s", *mySecret)
			// log the pseudo GET request
			hplog.Println("GET ", path)
		} else if path != "/" {
			// return value to the pseudo GET request
			fmt.Fprintf(w, "hello from %s\n", path)
			// log the pseudo GET request
			hplog.Println("GET ", path)
		} else {
			// return value to the pseudo GET request
			fmt.Fprintf(w, "try to add /test as path\n")
			// log the pseudo GET request
			hplog.Println("GET ", path)
		}
	})
	hplog.Println("------------------------------------------------------------")
	hplog.Println("hello-path-go - a simple web service returning the URL path.")
	hplog.Println("------------------------------------------------------------")
	hplog.Println("Web service initialization...")

	// reloadEnable help to wait for the appropriate secret to be provided.
	if *reloadEnable != false {
		hplog.Println("RELOAD: Connection to remote service: nok. Checking every 10 seconds.")
		for *mySecret != "4321" {
			hplog.Println("RELOAD: mysecret value is", *mySecret, "while expected value is 4321.")
			time.Sleep(10 * time.Second)
		}
	}

	// check that the secret is correct to start the service.
	// if no, we crash.
	if *mySecret != "4321" {
		hplog.Println("Note: mysecret value is", *mySecret, "while expected value is 4321.")
		hplog.Fatalln("FATAL: connection to remote service failed. Check mysecret parameter.")
	}

	// if yes, we start the service.
	hplog.Println("Connection to remote service: ok.")
	hplog.Println("Web service accessible at", *listenAddr)

	// Start the service and listen on the given port.
	if err := http.ListenAndServe(*listenAddr, nil); err != nil {
		// Log error messages
		hplog.Fatal(err)
	}
}

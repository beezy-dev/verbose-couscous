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
		listenAddr = flag.String("listen-addr", "0.0.0.0:8080", "Service IP and Port with default 0.0.0.0:8080")
		mySecret   = flag.String("my-secret", "1234", "Default secret is 1234")
	)

	flag.Parse()

	// Intanciate a logger
	hplog := log.New(os.Stdout, "[GO] ", log.LstdFlags)

	// Define a handler for pseudo GET requests
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		path := r.URL.Path

		// conditional message based on the provided path
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

	hplog.Println("Creating a hello path web service with logger")
	for *mySecret != "4321" {
		hplog.Println("Connection to remote service: nok. Check my-secret parameter.")
		hplog.Println("Note: my-secret value is", *mySecret, "while expecting 4321")
		time.Sleep(10 * time.Second)
	}

	// Print web service start message at the console
	hplog.Println("Connection to remote service: ok")
	hplog.Println("Web service accessible at", *listenAddr)

	// Start the service and listen on the given port
	if err := http.ListenAndServe(*listenAddr, nil); err != nil {
		// Log error messages
		hplog.Fatal(err)
	}
}

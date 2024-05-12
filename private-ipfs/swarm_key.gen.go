package main

import (
    "crypto/rand"
    "fmt"
)

func main() {
    key := make([]byte, 32)
    _, err := rand.Read(key)
    if err != nil {
        panic(err)
    }
    fmt.Printf("/key/swarm/psk/1.0.0/\n/base16/\n%s\n", fmt.Sprintf("%x", key))
}

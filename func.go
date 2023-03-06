package main

import (
	"encoding/json"
	"fmt"
	"os"

	"context"
	"io"
	"log"

	"github.com/wader/goutubedl"
)

type Person struct {
	Name string
}

func main() {
	p := &Person{Name: "World"}
	json.NewDecoder(os.Stdin).Decode(p)
	fmt.Printf("Hello %v!", p.Name)

	result, err := goutubedl.New(context.Background(), "https://www.youtube.com/watch?v=K4TOrB7at0Y", goutubedl.Options{})
	if err != nil {
		log.Fatal(err)
	}
	downloadResult, err := result.Download(context.Background(), "best")
	if err != nil {
		log.Fatal(err)
	}
	defer downloadResult.Close()
	f, err := os.Create("output")
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()
	io.Copy(f, downloadResult)
}

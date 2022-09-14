package meta

import (
	"encoding/json"
	"fmt"
)

type Book struct {
	Title           string
	Author          string
	Isbn10          string
	Quality         string
	Language        string
	PublicationDate string
	BookType        string
	PurchasePrice   float32
}

func DecodeBook(bytes []byte) {
	//var dat map[string]interface{}
	var book Book
	if err := json.Unmarshal(bytes, &book); err != nil {
		panic(err)
	}
	fmt.Println(book.Title)

}

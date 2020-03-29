package main

import "fmt"

type car struct {
	name string
}

func (c car) setName01(s string) {
	c.name = s
}
func (c *car) setName02(s string) {
	c.name = s
}

func main() {
	c := &car{}
	c.setName01("foo")
	fmt.Println(c.name)
	c.setName02("bar")
	fmt.Println(c.name)
}

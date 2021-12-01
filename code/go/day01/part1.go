package main

import (
	"fmt"
	utils "./utils"
)


func main() {

	input_filename := utils.Get_args()
	data := utils.Load_data(input_filename)
	deltas := utils.Calculate_deltas(data)
	upsides := utils.Count_upside(deltas)

	fmt.Printf("Data: %v\n", data)
	fmt.Printf("Deltas: %v\n", deltas)
	fmt.Printf("Upsides: %v\n", upsides)
}
package utils

import (
	"fmt"
	"os"
	"bufio"
	"log"
	"strconv"
)

func Get_args() string {
	// Get Input File
	if len(os.Args) < 2 {
		panic("Error, missing input_filename")
	}
	input_filename := os.Args[1]
	return input_filename
}

func Load_data(input_filename string) []int {

	fmt.Printf("Input Filename: %v\n", input_filename)

	if _, err := os.Stat(input_filename); os.IsNotExist(err) {
		panic("Error, input file does not exist")
	}

	file, err := os.Open(input_filename)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var data []int
	for scanner.Scan() {
		v, err := strconv.Atoi(scanner.Text())
		if err != nil {
			log.Fatal(err)
		}
		data = append(data, v)
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	return data
}

func Calculate_deltas(data []int) []int {
	if len(data) < 2 {
		log.Fatal("Error: data less than 2")
	}
	
	deltas := make([]int, len(data) - 1)

	var i int
	for i =0; i < len(data)-1; i++ {
		deltas[i] = data[i+1] - data[i]
	}

	return deltas
}

func Count_upside(deltas []int) int {
	var upsides, i int
	upsides = 0

	for i=0; i < len(deltas); i++ {
		if deltas[i] > 0 {
			upsides++
		}
	}
	return upsides
}

func Smooth_data(data []int) []int {
	
	if len(data) < 3 {
		log.Fatal("Error: data length less than 3")
	}
	
	var i int
	var smooth []int

	for i=0; i < len(data) - 2; i++ {
		sum := data[i] + data[i+1] + data[i+2]
		smooth = append(smooth, sum)
	}

	return smooth
}
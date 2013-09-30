#include <stdio.h>
#include <stdlib.h>


typedef struct {
	int size;
	int v[0];
} value_t;

typedef struct {
	int size;
	int w[0];
} weight_t;

/* global arrays */
value_t *values;
weight_t *weights;

int read_file(char *filename, int *total_weight, 
			  int *num_items) {

	FILE *f = NULL;
	int value;
	int weight;
	char line[80];
	int i;
	
	f = fopen(filename, "rt");

	/* first line: [knapsack_size] [number_of_items] */
	if (fgets(line, 80, f) != NULL) {
		sscanf(line, "%d %d", total_weight, num_items);

		printf("Total weight = %d & Num items = %d\n", 
				*total_weight, *num_items);
	} else {
		printf("ERROR: Cannot parse first line\n");
		return (1);
	}

	values = (value_t *) malloc(sizeof(value_t) + 
									sizeof(int) * (*num_items + 1));
	
	weights = (weight_t *) malloc(sizeof(weight_t) +
									sizeof(int) * (*num_items + 1));


	i = 1;
	while(fgets(line, 80, f) != NULL) {
		if (i % 100 == 0)
			printf("Scanning line %d\n", i);

		sscanf(line, "%d %d", &value, &weight);
		
		values->v[i] = value;
		weights->w[i] = weight;

		i++;
	}
	

	fclose(f);

	return (0);
}


int find_max_knapsack_value(int i, int x) {
	int value_without_i = 0;
	int value_with_i = 0;


	/* Base Case */
	if (i == 0) {
		if (weights->w[i] > x) {
			return 0;
		} else {
			return values->v[i];
		}
	}

	value_without_i = find_max_knapsack_value(i - 1, x);

	if (weights->w[i] > x) {
		return value_without_i;
	}

	value_with_i = values->v[i] + 
			find_max_knapsack_value(i - 1, x - weights->w[i]);

	
	return value_without_i > value_with_i ? 
				value_without_i:value_with_i;
}

int knapsack_iterative(int num_items, int total_weight) {
	/* vector of values */
	int *vector = NULL;
	int i;
	int j;
	//int value_without_i;
	int value_with_i;
	int max_knapsack_value = 0;

	vector = (int *) malloc(sizeof(int) * (total_weight + 1));

	for (j = 0; j < total_weight + 1; j++) {
		vector[j] = 0;	
	}

	for (i = 1; i < num_items + 1; i++) {
		printf("Procesing item %d of %d...\n", i, num_items);
		for (j = total_weight; j >= 0 ; j--) {
			//value_without_i = vector[j]

			if (j < weights->w[i]) {
				// do nothing (i.e. simply copy left value)
				// vector[j] = value_without_i;
			} else {
				value_with_i = vector[j - weights->w[i]] + values->v[i];

				if (value_with_i > vector[j]) {
					vector[j] = value_with_i;
				}
			}
		}
	}

	max_knapsack_value = vector[total_weight];

	if (vector)
		free(vector);
	
	return max_knapsack_value;
}

int main(void) {
	int total_weight;
	int num_items;
	int rc = 0;
	int max_knapsack_value = 0;
	
	rc = read_file("knapsack_big.txt", &total_weight, &num_items);

	if (rc != 0) {
		printf("ERROR in read_file\n");
		return (1);
	}

	//max_knapsack_value = 
	//	find_max_knapsack_value(num_items - 1, total_weight);
	
	max_knapsack_value = knapsack_iterative(num_items, total_weight);
	
	
	printf("Max Value = %d\n", max_knapsack_value);


	/* Cleanup */
	if (values)
		free(values);
	if (weights)
		free(weights);

}

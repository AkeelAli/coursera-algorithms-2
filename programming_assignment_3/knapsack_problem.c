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
											sizeof(int) * *num_items);
	
	weights = (weight_t *) malloc(sizeof(weight_t) +
										sizeof(int) * *num_items);


	i = 0;
	while(fgets(line, 80, f) != NULL) {
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

int main(void) {
	int total_weight;
	int num_items;
	int rc = 0;
	int max_knapsack_value = 0;

	rc = read_file("knapsack1.txt", &total_weight, &num_items);

	if (rc != 0) {
		printf("ERROR in read_file\n");
		return (1);
	}

	max_knapsack_value = 
		find_max_knapsack_value(num_items - 1, total_weight);

	printf("Max Value = %d\n", max_knapsack_value);


	/* Cleanup */
	if (values)
		free(values);
	if (weights)
		free(weights);

}

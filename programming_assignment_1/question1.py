def get_job_priority(w, l):
    return (w - l)

def insert_job_in_priority(job, job_list):
    # assume job_list already sorted in decreasing order of priority
    job_list.append(job)
    job_p = get_job_priority(job[0], job[1])

    job_list_length = len(job_list)

    for i in range(job_list_length - 2, -1, -1):
        job_cmp = job_list[i]
        job_cmp_p = get_job_priority(job_cmp[0], job_cmp[1])
        if (job_cmp_p < job_p) or (job_cmp_p == job_p and job_cmp[0] < job[0]):
            job_list[i], job_list[i + 1] = job_list[i + 1], job_list[i]
        else:
            break


# (1) Parse jobs.txt for jobs and build sorted array 
#     of jobs based on priority

f = open('jobs.txt', 'r')

lines = f.readlines()

# first line is the number of jobs
num_jobs = lines[0]

# prioritized list of jobs
job_list = []

# parse the rest of the jobs
i = 1
for line in lines[1:]:
    print "Processing job" + str(i)
    # line = "weight length\n"
    job = line.split(' ')
    job[0] = int(job[0])
    job[1] = int(job[1])

    insert_job_in_priority(job, job_list)
    
    i += 1

# Debug print to show job list in order
#print job_list


# (2) Compute sum of weighted completion ( SUM (w_i * C_i) )
sum = 0
completion_time = 0
for job in job_list:
    w = job[0]
    l = job[1]

    completion_time += l
    sum += w * completion_time

print "Weighted completion sum = " + str(sum)



f.close()

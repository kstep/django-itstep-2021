var app = new Vue({
    'el': '#app',
    'data': {
        'new_task_description': 'Describe new task here...',
        'tasks': [],
        'page': 1,
        'maxPage': 10
    },
    'created': function () {
        this.loadTasks();
    },
    'methods': {
        'loadTasks': function () {
            var self = this;
            fetch(djangoUrls.taskList + "?page=" + self.page).then(function (response) {
                return response.json();
            }).then(function (data) {
                self.tasks = data.results;
                self.maxPage = Math.ceil(data.count / 5);
            });
        },
        'markTaskDone': function (task, is_done) {
            task.is_done = is_done;
        },
        'next_page': function() {
            this.page += 1;
            this.loadTasks();
        },
        'prev_page': function() {
            if (this.page > 1) {
                this.page -= 1;
                this.loadTasks();
            }
        },
        'createTask': function (description) {
            var task = {
                'description': description,
                'is_done': false
            };
            var self = this;
            fetch(djangoUrls.taskList, {
                'method': 'POST',
                'body': JSON.stringify(task),
                'headers': {
                    'Content-Type': 'application/json'
                }
            }).then(function (response) {
                return response.json();
            }).then(function (data) {
                self.tasks.push(data);
            });
        }
    }
});

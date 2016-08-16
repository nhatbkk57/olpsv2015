from horizon import tables
import json 
from .tables import LogsTable


class IndexView(tables.DataTableView):
    table_class = LogsTable
    template_name = 'logmanagement/overview/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        instances = []
        try:
            instances, self._more = api.nova.server_list(
                self.request,
                search_opts=search_opts,
                all_tenants=True)
            context['instances'] = instances
        except Exception:
            self._more = False
            context['instances'] = "empty"

        # obj = '[{"id": 1, "time": "2015-11-14 00:23:46.664", "pid": 4180, "level": "INFO", "name": "neutron.openstack.common.service", "content": "[req-0174f305-5689-4076-803c-aef774ae45e0 ] Child caught SIGTERM"}, {"id": 2, "time": "2015-11-14 00:23:46.889", "pid": 4191, "level": "ERROR", "name": "neutron.openstack.common.service", "content": "[req-0174f305-5689-4076-803c-aef774ae45e0 ] Child caught SIGTERM"}, {"id": 3, "time": "2015-11-14 00:23:47.264", "pid": 4200, "level": "INFO", "name": "neutron.openstack.common.service", "content": "[req-0174f305-5689-4076-803c-aef774ae45e0 ] Child caught SIGTERM"}, {"id": 4, "time": "2015-11-14 00:23:48.664", "pid": 4180, "level": "WARNING", "name": "neutron.openstack.common.service", "content": "[req-0174f305-5689-4076-803c-aef774ae45e0 ] Child caught SIGTERM"}, {"id": 5, "time": "2015-11-14 00:23:48.964", "pid": 4191, "level": "INFO", "name": "neutron.openstack.common.service", "content": "[req-0174f305-5689-4076-803c-aef774ae45e0 ] Child caught SIGTERMmmmmmm mmmmmmm mmmmmmmmmm mmmm mmmm mmmm mmmm mmmm mmmmm mmmmmm mmmmmm"}]'
        obj = '[]'
        logs = json.loads(obj)
        
        context['logs'] = logs
        # print(params)
        return context


    def get_data(self):
        obj = '[{"id": 1, "time": "2015-11-14 00:23:46.664", "pid": 4180, "level": "INFO", "name": "neutron.openstack.common.service", "content": "[req-0174f305-5689-4076-803c-aef774ae45e0 ] Child caught SIGTERM"}, {"id": 2, "time": "2015-11-14 00:23:46.889", "pid": 4191, "level": "ERROR", "name": "neutron.openstack.common.service", "content": "[req-0174f305-5689-4076-803c-aef774ae45e0 ] Child caught SIGTERM"}, {"id": 3, "time": "2015-11-14 00:23:47.264", "pid": 4200, "level": "INFO", "name": "neutron.openstack.common.service", "content": "[req-0174f305-5689-4076-803c-aef774ae45e0 ] Child caught SIGTERM"}, {"id": 4, "time": "2015-11-14 00:23:48.664", "pid": 4180, "level": "WARNING", "name": "neutron.openstack.common.service", "content": "[req-0174f305-5689-4076-803c-aef774ae45e0 ] Child caught SIGTERM"}, {"id": 5, "time": "2015-11-14 00:23:48.964", "pid": 4191, "level": "INFO", "name": "neutron.openstack.common.service", "content": "[req-0174f305-5689-4076-803c-aef774ae45e0 ] Child caught SIGTERMmmmmmm mmmmmmm mmmmmmmmmm mmmm mmmm mmmm mmmm mmmm mmmmm mmmmmm mmmmmm"}]'
        logs = json.loads(obj)
        context = []
        for log in logs:
            if (self.request.method == 'GET' and 'start' in self.request.GET and 'end' in self.request.GET):
                if (log['time'] >= self.request.GET['start']) & (log['time'] <= self.request.GET['end']):
                    context.append(Log(log['id'], log['time'], log['pid'], log['level'], log['name'], log['content']))
            else:
                context.append(Log(log['id'], log['time'], log['pid'], log['level'], log['name'], log['content']))
        return context


class Log:
	def __init__(self, log_id, time, pid, level, name, content):
		self.id = log_id
		self.time = time
		self.pid = pid
		self.level = level
		self.name = name
		self.content = content
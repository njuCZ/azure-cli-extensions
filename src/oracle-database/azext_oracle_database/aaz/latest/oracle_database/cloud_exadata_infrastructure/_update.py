# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "oracle-database cloud-exadata-infrastructure update",
)
class Update(AAZCommand):
    """Update a CloudExadataInfrastructure

    :example: Update Exa infra
        az oracle-database cloud-exadata-infrastructure update --name <name> --resource-group <RG name> --tags {tagV1:tagK1>
    """

    _aaz_info = {
        "version": "2023-09-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/oracle.database/cloudexadatainfrastructures/{}", "2023-09-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.cloudexadatainfrastructurename = AAZStrArg(
            options=["-n", "--name", "--cloudexadatainfrastructurename"],
            help="CloudExadataInfrastructure name",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern=".*",
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.compute_count = AAZIntArg(
            options=["--compute-count"],
            arg_group="Properties",
            help="The number of compute servers for the cloud Exadata infrastructure.",
            nullable=True,
        )
        _args_schema.customer_contacts = AAZListArg(
            options=["--customer-contacts"],
            arg_group="Properties",
            help="The list of customer email addresses that receive information from Oracle about the specified OCI Database service resource. Oracle uses these email addresses to send notifications about planned and unplanned software maintenance updates, information about system hardware, and other information needed by administrators. Up to 10 email addresses can be added to the customer contacts for a cloud Exadata infrastructure instance. ",
            nullable=True,
        )
        _args_schema.display_name = AAZStrArg(
            options=["--display-name"],
            arg_group="Properties",
            help="The name for the Exadata infrastructure.",
            fmt=AAZStrArgFormat(
                max_length=255,
                min_length=1,
            ),
        )
        _args_schema.maintenance_window = AAZObjectArg(
            options=["--maintenance-window"],
            arg_group="Properties",
            help="maintenanceWindow property",
            nullable=True,
        )
        _args_schema.storage_count = AAZIntArg(
            options=["--storage-count"],
            arg_group="Properties",
            help="The number of storage servers for the cloud Exadata infrastructure.",
            nullable=True,
        )

        customer_contacts = cls._args_schema.customer_contacts
        customer_contacts.Element = AAZObjectArg(
            nullable=True,
        )

        _element = cls._args_schema.customer_contacts.Element
        _element.email = AAZStrArg(
            options=["email"],
            help="The email address used by Oracle to send notifications regarding databases and infrastructure.",
            fmt=AAZStrArgFormat(
                max_length=320,
                min_length=1,
            ),
        )

        maintenance_window = cls._args_schema.maintenance_window
        maintenance_window.custom_action_timeout_in_mins = AAZIntArg(
            options=["custom-action-timeout-in-mins"],
            help="Determines the amount of time the system will wait before the start of each database server patching operation. Custom action timeout is in minutes and valid value is between 15 to 120 (inclusive).",
            nullable=True,
            fmt=AAZIntArgFormat(
                maximum=120,
                minimum=0,
            ),
        )
        maintenance_window.days_of_week = AAZListArg(
            options=["days-of-week"],
            help="Days during the week when maintenance should be performed.",
            nullable=True,
        )
        maintenance_window.hours_of_day = AAZListArg(
            options=["hours-of-day"],
            help="The window of hours during the day when maintenance should be performed. The window is a 4 hour slot. Valid values are - 0 - represents time slot 0:00 - 3:59 UTC - 4 - represents time slot 4:00 - 7:59 UTC - 8 - represents time slot 8:00 - 11:59 UTC - 12 - represents time slot 12:00 - 15:59 UTC - 16 - represents time slot 16:00 - 19:59 UTC - 20 - represents time slot 20:00 - 23:59 UTC",
            nullable=True,
        )
        maintenance_window.is_custom_action_timeout_enabled = AAZBoolArg(
            options=["is-custom-action-timeout-enabled"],
            help="If true, enables the configuration of a custom action timeout (waiting period) between database server patching operations.",
            nullable=True,
        )
        maintenance_window.is_monthly_patching_enabled = AAZBoolArg(
            options=["is-monthly-patching-enabled"],
            help="is Monthly Patching Enabled",
            nullable=True,
        )
        maintenance_window.lead_time_in_weeks = AAZIntArg(
            options=["lead-time-in-weeks"],
            help="Lead time window allows user to set a lead time to prepare for a down time. The lead time is in weeks and valid value is between 1 to 4. ",
            nullable=True,
        )
        maintenance_window.months = AAZListArg(
            options=["months"],
            help="Months during the year when maintenance should be performed.",
            nullable=True,
        )
        maintenance_window.patching_mode = AAZStrArg(
            options=["patching-mode"],
            help="Cloud Exadata infrastructure node patching method.",
            nullable=True,
            enum={"NonRolling": "NonRolling", "Rolling": "Rolling"},
        )
        maintenance_window.preference = AAZStrArg(
            options=["preference"],
            help="The maintenance window scheduling preference.",
            nullable=True,
            enum={"CustomPreference": "CustomPreference", "NoPreference": "NoPreference"},
        )
        maintenance_window.weeks_of_month = AAZListArg(
            options=["weeks-of-month"],
            help="Weeks during the month when maintenance should be performed. Weeks start on the 1st, 8th, 15th, and 22nd days of the month, and have a duration of 7 days. Weeks start and end based on calendar dates, not days of the week. For example, to allow maintenance during the 2nd week of the month (from the 8th day to the 14th day of the month), use the value 2. Maintenance cannot be scheduled for the fifth week of months that contain more than 28 days. Note that this parameter works in conjunction with the  daysOfWeek and hoursOfDay parameters to allow you to specify specific days of the week and hours that maintenance will be performed. ",
            nullable=True,
        )

        days_of_week = cls._args_schema.maintenance_window.days_of_week
        days_of_week.Element = AAZObjectArg(
            nullable=True,
        )

        _element = cls._args_schema.maintenance_window.days_of_week.Element
        _element.name = AAZStrArg(
            options=["name"],
            help="Name of the day of the week.",
            enum={"Friday": "Friday", "Monday": "Monday", "Saturday": "Saturday", "Sunday": "Sunday", "Thursday": "Thursday", "Tuesday": "Tuesday", "Wednesday": "Wednesday"},
        )

        hours_of_day = cls._args_schema.maintenance_window.hours_of_day
        hours_of_day.Element = AAZIntArg(
            nullable=True,
        )

        months = cls._args_schema.maintenance_window.months
        months.Element = AAZObjectArg(
            nullable=True,
        )

        _element = cls._args_schema.maintenance_window.months.Element
        _element.name = AAZStrArg(
            options=["name"],
            help="Name of the month of the year.",
            enum={"April": "April", "August": "August", "December": "December", "February": "February", "January": "January", "July": "July", "June": "June", "March": "March", "May": "May", "November": "November", "October": "October", "September": "September"},
        )

        weeks_of_month = cls._args_schema.maintenance_window.weeks_of_month
        weeks_of_month.Element = AAZIntArg(
            nullable=True,
        )

        # define Arg Group "Resource"

        _args_schema = cls._args_schema
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Resource",
            help="Resource tags.",
            nullable=True,
        )
        _args_schema.zones = AAZListArg(
            options=["--zones"],
            arg_group="Resource",
            help="CloudExadataInfrastructure zones",
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg(
            nullable=True,
        )

        zones = cls._args_schema.zones
        zones.Element = AAZStrArg(
            nullable=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.CloudExadataInfrastructuresGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        yield self.CloudExadataInfrastructuresCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class CloudExadataInfrastructuresGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Oracle.Database/cloudExadataInfrastructures/{cloudexadatainfrastructurename}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "cloudexadatainfrastructurename", self.ctx.args.cloudexadatainfrastructurename,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-09-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _UpdateHelper._build_schema_cloud_exadata_infrastructure_read(cls._schema_on_200)

            return cls._schema_on_200

    class CloudExadataInfrastructuresCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Oracle.Database/cloudExadataInfrastructures/{cloudexadatainfrastructurename}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "cloudexadatainfrastructurename", self.ctx.args.cloudexadatainfrastructurename,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-09-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _UpdateHelper._build_schema_cloud_exadata_infrastructure_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")
            _builder.set_prop("zones", AAZListType, ".zones", typ_kwargs={"flags": {"required": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("computeCount", AAZIntType, ".compute_count")
                properties.set_prop("customerContacts", AAZListType, ".customer_contacts")
                properties.set_prop("displayName", AAZStrType, ".display_name", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("maintenanceWindow", AAZObjectType, ".maintenance_window")
                properties.set_prop("storageCount", AAZIntType, ".storage_count")

            customer_contacts = _builder.get(".properties.customerContacts")
            if customer_contacts is not None:
                customer_contacts.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.customerContacts[]")
            if _elements is not None:
                _elements.set_prop("email", AAZStrType, ".email", typ_kwargs={"flags": {"required": True}})

            maintenance_window = _builder.get(".properties.maintenanceWindow")
            if maintenance_window is not None:
                maintenance_window.set_prop("customActionTimeoutInMins", AAZIntType, ".custom_action_timeout_in_mins")
                maintenance_window.set_prop("daysOfWeek", AAZListType, ".days_of_week")
                maintenance_window.set_prop("hoursOfDay", AAZListType, ".hours_of_day")
                maintenance_window.set_prop("isCustomActionTimeoutEnabled", AAZBoolType, ".is_custom_action_timeout_enabled")
                maintenance_window.set_prop("isMonthlyPatchingEnabled", AAZBoolType, ".is_monthly_patching_enabled")
                maintenance_window.set_prop("leadTimeInWeeks", AAZIntType, ".lead_time_in_weeks")
                maintenance_window.set_prop("months", AAZListType, ".months")
                maintenance_window.set_prop("patchingMode", AAZStrType, ".patching_mode")
                maintenance_window.set_prop("preference", AAZStrType, ".preference")
                maintenance_window.set_prop("weeksOfMonth", AAZListType, ".weeks_of_month")

            days_of_week = _builder.get(".properties.maintenanceWindow.daysOfWeek")
            if days_of_week is not None:
                days_of_week.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.maintenanceWindow.daysOfWeek[]")
            if _elements is not None:
                _elements.set_prop("name", AAZStrType, ".name", typ_kwargs={"flags": {"required": True}})

            hours_of_day = _builder.get(".properties.maintenanceWindow.hoursOfDay")
            if hours_of_day is not None:
                hours_of_day.set_elements(AAZIntType, ".")

            months = _builder.get(".properties.maintenanceWindow.months")
            if months is not None:
                months.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.maintenanceWindow.months[]")
            if _elements is not None:
                _elements.set_prop("name", AAZStrType, ".name", typ_kwargs={"flags": {"required": True}})

            weeks_of_month = _builder.get(".properties.maintenanceWindow.weeksOfMonth")
            if weeks_of_month is not None:
                weeks_of_month.set_elements(AAZIntType, ".")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            zones = _builder.get(".zones")
            if zones is not None:
                zones.set_elements(AAZStrType, ".")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    _schema_cloud_exadata_infrastructure_read = None

    @classmethod
    def _build_schema_cloud_exadata_infrastructure_read(cls, _schema):
        if cls._schema_cloud_exadata_infrastructure_read is not None:
            _schema.id = cls._schema_cloud_exadata_infrastructure_read.id
            _schema.location = cls._schema_cloud_exadata_infrastructure_read.location
            _schema.name = cls._schema_cloud_exadata_infrastructure_read.name
            _schema.properties = cls._schema_cloud_exadata_infrastructure_read.properties
            _schema.system_data = cls._schema_cloud_exadata_infrastructure_read.system_data
            _schema.tags = cls._schema_cloud_exadata_infrastructure_read.tags
            _schema.type = cls._schema_cloud_exadata_infrastructure_read.type
            _schema.zones = cls._schema_cloud_exadata_infrastructure_read.zones
            return

        cls._schema_cloud_exadata_infrastructure_read = _schema_cloud_exadata_infrastructure_read = AAZObjectType()

        cloud_exadata_infrastructure_read = _schema_cloud_exadata_infrastructure_read
        cloud_exadata_infrastructure_read.id = AAZStrType(
            flags={"read_only": True},
        )
        cloud_exadata_infrastructure_read.location = AAZStrType(
            flags={"required": True},
        )
        cloud_exadata_infrastructure_read.name = AAZStrType(
            flags={"read_only": True},
        )
        cloud_exadata_infrastructure_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        cloud_exadata_infrastructure_read.system_data = AAZObjectType(
            serialized_name="systemData",
            flags={"read_only": True},
        )
        cloud_exadata_infrastructure_read.tags = AAZDictType()
        cloud_exadata_infrastructure_read.type = AAZStrType(
            flags={"read_only": True},
        )
        cloud_exadata_infrastructure_read.zones = AAZListType(
            flags={"required": True},
        )

        properties = _schema_cloud_exadata_infrastructure_read.properties
        properties.activated_storage_count = AAZIntType(
            serialized_name="activatedStorageCount",
            flags={"read_only": True},
        )
        properties.additional_storage_count = AAZIntType(
            serialized_name="additionalStorageCount",
            flags={"read_only": True},
        )
        properties.available_storage_size_in_gbs = AAZIntType(
            serialized_name="availableStorageSizeInGbs",
            flags={"read_only": True},
        )
        properties.compute_count = AAZIntType(
            serialized_name="computeCount",
        )
        properties.cpu_count = AAZIntType(
            serialized_name="cpuCount",
            flags={"read_only": True},
        )
        properties.customer_contacts = AAZListType(
            serialized_name="customerContacts",
        )
        properties.data_storage_size_in_tbs = AAZFloatType(
            serialized_name="dataStorageSizeInTbs",
            flags={"read_only": True},
        )
        properties.db_node_storage_size_in_gbs = AAZIntType(
            serialized_name="dbNodeStorageSizeInGbs",
            flags={"read_only": True},
        )
        properties.db_server_version = AAZStrType(
            serialized_name="dbServerVersion",
            flags={"read_only": True},
        )
        properties.display_name = AAZStrType(
            serialized_name="displayName",
            flags={"required": True},
        )
        properties.estimated_patching_time = AAZObjectType(
            serialized_name="estimatedPatchingTime",
        )
        properties.last_maintenance_run_id = AAZStrType(
            serialized_name="lastMaintenanceRunId",
        )
        properties.lifecycle_details = AAZStrType(
            serialized_name="lifecycleDetails",
            flags={"read_only": True},
        )
        properties.lifecycle_state = AAZStrType(
            serialized_name="lifecycleState",
        )
        properties.maintenance_window = AAZObjectType(
            serialized_name="maintenanceWindow",
        )
        properties.max_cpu_count = AAZIntType(
            serialized_name="maxCpuCount",
            flags={"read_only": True},
        )
        properties.max_data_storage_in_tbs = AAZFloatType(
            serialized_name="maxDataStorageInTbs",
            flags={"read_only": True},
        )
        properties.max_db_node_storage_size_in_gbs = AAZIntType(
            serialized_name="maxDbNodeStorageSizeInGbs",
            flags={"read_only": True},
        )
        properties.max_memory_in_gbs = AAZIntType(
            serialized_name="maxMemoryInGbs",
            flags={"read_only": True},
        )
        properties.memory_size_in_gbs = AAZIntType(
            serialized_name="memorySizeInGbs",
            flags={"read_only": True},
        )
        properties.monthly_db_server_version = AAZStrType(
            serialized_name="monthlyDbServerVersion",
            flags={"read_only": True},
        )
        properties.monthly_storage_server_version = AAZStrType(
            serialized_name="monthlyStorageServerVersion",
            flags={"read_only": True},
        )
        properties.next_maintenance_run_id = AAZStrType(
            serialized_name="nextMaintenanceRunId",
        )
        properties.oci_url = AAZStrType(
            serialized_name="ociUrl",
            flags={"read_only": True},
        )
        properties.ocid = AAZStrType()
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.shape = AAZStrType(
            flags={"required": True},
        )
        properties.storage_count = AAZIntType(
            serialized_name="storageCount",
        )
        properties.storage_server_version = AAZStrType(
            serialized_name="storageServerVersion",
            flags={"read_only": True},
        )
        properties.time_created = AAZStrType(
            serialized_name="timeCreated",
            flags={"read_only": True},
        )
        properties.total_storage_size_in_gbs = AAZIntType(
            serialized_name="totalStorageSizeInGbs",
            flags={"read_only": True},
        )

        customer_contacts = _schema_cloud_exadata_infrastructure_read.properties.customer_contacts
        customer_contacts.Element = AAZObjectType()

        _element = _schema_cloud_exadata_infrastructure_read.properties.customer_contacts.Element
        _element.email = AAZStrType(
            flags={"required": True},
        )

        estimated_patching_time = _schema_cloud_exadata_infrastructure_read.properties.estimated_patching_time
        estimated_patching_time.estimated_db_server_patching_time = AAZIntType(
            serialized_name="estimatedDbServerPatchingTime",
            flags={"read_only": True},
        )
        estimated_patching_time.estimated_network_switches_patching_time = AAZIntType(
            serialized_name="estimatedNetworkSwitchesPatchingTime",
            flags={"read_only": True},
        )
        estimated_patching_time.estimated_storage_server_patching_time = AAZIntType(
            serialized_name="estimatedStorageServerPatchingTime",
            flags={"read_only": True},
        )
        estimated_patching_time.total_estimated_patching_time = AAZIntType(
            serialized_name="totalEstimatedPatchingTime",
            flags={"read_only": True},
        )

        maintenance_window = _schema_cloud_exadata_infrastructure_read.properties.maintenance_window
        maintenance_window.custom_action_timeout_in_mins = AAZIntType(
            serialized_name="customActionTimeoutInMins",
        )
        maintenance_window.days_of_week = AAZListType(
            serialized_name="daysOfWeek",
        )
        maintenance_window.hours_of_day = AAZListType(
            serialized_name="hoursOfDay",
        )
        maintenance_window.is_custom_action_timeout_enabled = AAZBoolType(
            serialized_name="isCustomActionTimeoutEnabled",
        )
        maintenance_window.is_monthly_patching_enabled = AAZBoolType(
            serialized_name="isMonthlyPatchingEnabled",
        )
        maintenance_window.lead_time_in_weeks = AAZIntType(
            serialized_name="leadTimeInWeeks",
        )
        maintenance_window.months = AAZListType()
        maintenance_window.patching_mode = AAZStrType(
            serialized_name="patchingMode",
        )
        maintenance_window.preference = AAZStrType()
        maintenance_window.weeks_of_month = AAZListType(
            serialized_name="weeksOfMonth",
        )

        days_of_week = _schema_cloud_exadata_infrastructure_read.properties.maintenance_window.days_of_week
        days_of_week.Element = AAZObjectType()

        _element = _schema_cloud_exadata_infrastructure_read.properties.maintenance_window.days_of_week.Element
        _element.name = AAZStrType(
            flags={"required": True},
        )

        hours_of_day = _schema_cloud_exadata_infrastructure_read.properties.maintenance_window.hours_of_day
        hours_of_day.Element = AAZIntType()

        months = _schema_cloud_exadata_infrastructure_read.properties.maintenance_window.months
        months.Element = AAZObjectType()

        _element = _schema_cloud_exadata_infrastructure_read.properties.maintenance_window.months.Element
        _element.name = AAZStrType(
            flags={"required": True},
        )

        weeks_of_month = _schema_cloud_exadata_infrastructure_read.properties.maintenance_window.weeks_of_month
        weeks_of_month.Element = AAZIntType()

        system_data = _schema_cloud_exadata_infrastructure_read.system_data
        system_data.created_at = AAZStrType(
            serialized_name="createdAt",
        )
        system_data.created_by = AAZStrType(
            serialized_name="createdBy",
        )
        system_data.created_by_type = AAZStrType(
            serialized_name="createdByType",
        )
        system_data.last_modified_at = AAZStrType(
            serialized_name="lastModifiedAt",
        )
        system_data.last_modified_by = AAZStrType(
            serialized_name="lastModifiedBy",
        )
        system_data.last_modified_by_type = AAZStrType(
            serialized_name="lastModifiedByType",
        )

        tags = _schema_cloud_exadata_infrastructure_read.tags
        tags.Element = AAZStrType()

        zones = _schema_cloud_exadata_infrastructure_read.zones
        zones.Element = AAZStrType()

        _schema.id = cls._schema_cloud_exadata_infrastructure_read.id
        _schema.location = cls._schema_cloud_exadata_infrastructure_read.location
        _schema.name = cls._schema_cloud_exadata_infrastructure_read.name
        _schema.properties = cls._schema_cloud_exadata_infrastructure_read.properties
        _schema.system_data = cls._schema_cloud_exadata_infrastructure_read.system_data
        _schema.tags = cls._schema_cloud_exadata_infrastructure_read.tags
        _schema.type = cls._schema_cloud_exadata_infrastructure_read.type
        _schema.zones = cls._schema_cloud_exadata_infrastructure_read.zones


__all__ = ["Update"]
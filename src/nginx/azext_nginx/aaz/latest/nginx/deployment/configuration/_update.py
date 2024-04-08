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
    "nginx deployment configuration update",
)
class Update(AAZCommand):
    """Update an NGINX configuration

    :example: Update content of the first file in a configuration
        az nginx deployment configuration update --name default --deployment-name myDeployment --resource-group myResourceGroup --files [0].content="aHR0cCB7CiAgICB1cHN0cmVhbSBhcHAgewogICAgICAgIHpvbmUgYXBwIDY0azsKICAgICAgICBsZWFzdF9jb25uOwogICAgICAgIHNlcnZlciAxMC4wLjEuNDo4MDAwOwogICAgfQoKICAgIHNlcnZlciB7CiAgICAgICAgbGlzdGVuIDgwOwogICAgICAgIHNlcnZlcl9uYW1lICouZXhhbXBsZS5jb207CgogICAgICAgIGxvY2F0aW9uIC8gewogICAgICAgICAgICBwcm94eV9zZXRfaGVhZGVyIEhvc3QgJGhvc3Q7CiAgICAgICAgICAgIHByb3h5X3NldF9oZWFkZXIgWC1SZWFsLUlQICRyZW1vdGVfYWRkcjsKICAgICAgICAgICAgcHJveHlfc2V0X2hlYWRlciBYLVByb3h5LUFwcCBhcHA7CiAgICAgICAgICAgIHByb3h5X3NldF9oZWFkZXIgR2l0aHViLVJ1bi1JZCAwMDAwMDA7CiAgICAgICAgICAgIHByb3h5X2J1ZmZlcmluZyBvbjsKICAgICAgICAgICAgcHJveHlfYnVmZmVyX3NpemUgNGs7CiAgICAgICAgICAgIHByb3h5X2J1ZmZlcnMgOCA4azsKICAgICAgICAgICAgcHJveHlfcmVhZF90aW1lb3V0IDYwczsKICAgICAgICAgICAgcHJveHlfcGFzcyBodHRwOi8vYXBwOwogICAgICAgICAgICBoZWFsdGhfY2hlY2s7CiAgICAgICAgfQogICAgICAgIAogICAgfQp9"
    """

    _aaz_info = {
        "version": "2024-01-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/nginx.nginxplus/nginxdeployments/{}/configurations/{}", "2024-01-01-preview"],
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
        _args_schema.configuration_name = AAZStrArg(
            options=["-n", "--name", "--configuration-name"],
            help="The name of configuration, only 'default' is supported value due to the singleton of Nginx conf",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.deployment_name = AAZStrArg(
            options=["--deployment-name"],
            help="The name of targeted Nginx deployment",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^([a-z0-9A-Z][a-z0-9A-Z-]{0,28}[a-z0-9A-Z]|[a-z0-9A-Z])$",
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Body"

        _args_schema = cls._args_schema
        _args_schema.location = AAZResourceLocationArg(
            arg_group="Body",
            nullable=True,
            fmt=AAZResourceLocationArgFormat(
                resource_group_arg="resource_group",
            ),
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.files = AAZListArg(
            options=["--files"],
            arg_group="Properties",
            help={"short-summary": "This is an array of files required for the config set-up. Cannot be used with packages", "long-summary": "One of the files virtual-path should match the root file. For a multi-file config set-up, the root file needs to have references to the other file(s) in an include directive.\nUsage: --files [{\"content\":\"<Base64 content of config file>\",\"virtual-path\":\"<path>\"}]."},
            nullable=True,
        )
        _args_schema.root_file = AAZStrArg(
            options=["--root-file"],
            arg_group="Properties",
            help="Required. The root file that should align with your Nginx configuration structure",
            nullable=True,
        )

        files = cls._args_schema.files
        files.Element = AAZObjectArg(
            nullable=True,
        )
        cls._build_args_nginx_configuration_file_update(files.Element)
        return cls._args_schema

    _args_nginx_configuration_file_update = None

    @classmethod
    def _build_args_nginx_configuration_file_update(cls, _schema):
        if cls._args_nginx_configuration_file_update is not None:
            _schema.content = cls._args_nginx_configuration_file_update.content
            _schema.virtual_path = cls._args_nginx_configuration_file_update.virtual_path
            return

        cls._args_nginx_configuration_file_update = AAZObjectArg(
            nullable=True,
        )

        nginx_configuration_file_update = cls._args_nginx_configuration_file_update
        nginx_configuration_file_update.content = AAZStrArg(
            options=["content"],
            nullable=True,
        )
        nginx_configuration_file_update.virtual_path = AAZStrArg(
            options=["virtual-path"],
            nullable=True,
        )

        _schema.content = cls._args_nginx_configuration_file_update.content
        _schema.virtual_path = cls._args_nginx_configuration_file_update.virtual_path

    def _execute_operations(self):
        self.pre_operations()
        self.ConfigurationsGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        yield self.ConfigurationsCreateOrUpdate(ctx=self.ctx)()
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

    class ConfigurationsGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Nginx.NginxPlus/nginxDeployments/{deploymentName}/configurations/{configurationName}",
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
                    "configurationName", self.ctx.args.configuration_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "deploymentName", self.ctx.args.deployment_name,
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
                    "api-version", "2024-01-01-preview",
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
            _UpdateHelper._build_schema_nginx_configuration_read(cls._schema_on_200)

            return cls._schema_on_200

    class ConfigurationsCreateOrUpdate(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Nginx.NginxPlus/nginxDeployments/{deploymentName}/configurations/{configurationName}",
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
                    "configurationName", self.ctx.args.configuration_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "deploymentName", self.ctx.args.deployment_name,
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
                    "api-version", "2024-01-01-preview",
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
            _UpdateHelper._build_schema_nginx_configuration_read(cls._schema_on_200_201)

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
            _builder.set_prop("location", AAZStrType, ".location")
            _builder.set_prop("properties", AAZObjectType)

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("files", AAZListType, ".files")
                properties.set_prop("rootFile", AAZStrType, ".root_file")

            files = _builder.get(".properties.files")
            if files is not None:
                _UpdateHelper._build_schema_nginx_configuration_file_update(files.set_elements(AAZObjectType, "."))

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    @classmethod
    def _build_schema_nginx_configuration_file_update(cls, _builder):
        if _builder is None:
            return
        _builder.set_prop("content", AAZStrType, ".content")
        _builder.set_prop("virtualPath", AAZStrType, ".virtual_path")

    _schema_nginx_configuration_file_read = None

    @classmethod
    def _build_schema_nginx_configuration_file_read(cls, _schema):
        if cls._schema_nginx_configuration_file_read is not None:
            _schema.content = cls._schema_nginx_configuration_file_read.content
            _schema.virtual_path = cls._schema_nginx_configuration_file_read.virtual_path
            return

        cls._schema_nginx_configuration_file_read = _schema_nginx_configuration_file_read = AAZObjectType()

        nginx_configuration_file_read = _schema_nginx_configuration_file_read
        nginx_configuration_file_read.content = AAZStrType()
        nginx_configuration_file_read.virtual_path = AAZStrType(
            serialized_name="virtualPath",
        )

        _schema.content = cls._schema_nginx_configuration_file_read.content
        _schema.virtual_path = cls._schema_nginx_configuration_file_read.virtual_path

    _schema_nginx_configuration_read = None

    @classmethod
    def _build_schema_nginx_configuration_read(cls, _schema):
        if cls._schema_nginx_configuration_read is not None:
            _schema.id = cls._schema_nginx_configuration_read.id
            _schema.location = cls._schema_nginx_configuration_read.location
            _schema.name = cls._schema_nginx_configuration_read.name
            _schema.properties = cls._schema_nginx_configuration_read.properties
            _schema.system_data = cls._schema_nginx_configuration_read.system_data
            _schema.type = cls._schema_nginx_configuration_read.type
            return

        cls._schema_nginx_configuration_read = _schema_nginx_configuration_read = AAZObjectType()

        nginx_configuration_read = _schema_nginx_configuration_read
        nginx_configuration_read.id = AAZStrType(
            flags={"read_only": True},
        )
        nginx_configuration_read.location = AAZStrType()
        nginx_configuration_read.name = AAZStrType(
            flags={"read_only": True},
        )
        nginx_configuration_read.properties = AAZObjectType()
        nginx_configuration_read.system_data = AAZObjectType(
            serialized_name="systemData",
            flags={"read_only": True},
        )
        nginx_configuration_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_nginx_configuration_read.properties
        properties.files = AAZListType()
        properties.package = AAZObjectType()
        properties.protected_files = AAZListType(
            serialized_name="protectedFiles",
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.root_file = AAZStrType(
            serialized_name="rootFile",
        )

        files = _schema_nginx_configuration_read.properties.files
        files.Element = AAZObjectType()
        cls._build_schema_nginx_configuration_file_read(files.Element)

        package = _schema_nginx_configuration_read.properties.package
        package.data = AAZStrType()
        package.protected_files = AAZListType(
            serialized_name="protectedFiles",
        )

        protected_files = _schema_nginx_configuration_read.properties.package.protected_files
        protected_files.Element = AAZStrType()

        protected_files = _schema_nginx_configuration_read.properties.protected_files
        protected_files.Element = AAZObjectType()
        cls._build_schema_nginx_configuration_file_read(protected_files.Element)

        system_data = _schema_nginx_configuration_read.system_data
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

        _schema.id = cls._schema_nginx_configuration_read.id
        _schema.location = cls._schema_nginx_configuration_read.location
        _schema.name = cls._schema_nginx_configuration_read.name
        _schema.properties = cls._schema_nginx_configuration_read.properties
        _schema.system_data = cls._schema_nginx_configuration_read.system_data
        _schema.type = cls._schema_nginx_configuration_read.type


__all__ = ["Update"]
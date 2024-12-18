# This file is auto-generated. Do not edit manually.
# Last updated: 2024-09-23 19:27:00 UTC

SENTINEL_ASIM_TABLES = {
    "imAuditEvent": {
        "EventType": {
            "data_type": "Enumerated",
            "description": "Describes the operation audited by the event using a normalized value. Use EventSubType to provide further details, which the normalized value does not convey, and Operation. to store the operation as reported by the reporting device. For Audit Event records, the allowed values are: - Set- Read- Create- Delete- Execute- Install- Clear- Enable- Disable- Other Audit events represent a large variety of operations, and the Other value enables mapping operations that have no corresponding EventType. However, the use of Other limits the usability of the event and should be avoided if possible.",
            "class": "Mandatory",
        },
        "EventSubType": {
            "data_type": "String",
            "description": "Provides further details, which the normalized value in EventType does not convey.",
            "class": "Optional",
        },
        "EventSchema": {
            "data_type": "String",
            "description": "The name of the schema documented here is AuditEvent.",
            "class": "Mandatory",
        },
        "EventSchemaVersion": {
            "data_type": "String",
            "description": "The version of the schema. The version of the schema documented here is 0.1.",
            "class": "Mandatory",
        },
        "Operation": {
            "data_type": "String",
            "description": "The operation audited as reported by the reporting device.",
            "class": "Mandatory",
        },
        "Object": {
            "data_type": "String",
            "description": "The name of the object on which the operation identified by EventType is performed.",
            "class": "Mandatory",
        },
        "ObjectType": {
            "data_type": "Enumerated",
            "description": "The type of Object. Allowed values are:- Cloud Resource- Configuration Atom- Policy Rule - Other",
            "class": "Mandatory",
        },
        "OldValue": {
            "data_type": "String",
            "description": "The old value of Object prior to the operation, if applicable.",
            "class": "Optional",
        },
        "NewValue": {
            "data_type": "String",
            "description": "The new value of Object after the operation was performed, if applicable.",
            "class": "Optional",
        },
        "Value": {"data_type": "", "description": "Alias to NewValue", "class": "Alias"},
        "ValueType": {
            "data_type": "Enumerated",
            "description": "The type of the old and new values. Allowed values are- Other",
            "class": "Conditional",
        },
        "ActorUserId": {
            "data_type": "String",
            "description": "A machine-readable, alphanumeric, unique representation of the Actor. For more information, and for alternative fields for other IDs, see The User entity.  Example: S-1-12-1-4141952679-1282074057-627758481-2916039507",
            "class": "Optional",
        },
        "ActorScope": {
            "data_type": "String",
            "description": "The scope, such as Microsoft Entra Domain Name, in which ActorUserId and ActorUsername are defined. or more information and list of allowed values, see UserScope in the Schema Overview article.",
            "class": "Optional",
        },
        "ActorScopeId": {
            "data_type": "String",
            "description": "The scope ID, such as Microsoft Entra Directory ID, in which ActorUserId and ActorUsername are defined. for more information and list of allowed values, see UserScopeId in the Schema Overview article.",
            "class": "Optional",
        },
        "ActorUserIdType": {
            "data_type": "UserIdType",
            "description": "The type of the ID stored in the ActorUserId field. For more information and list of allowed values, see UserIdType in the Schema Overview article.",
            "class": "Conditional",
        },
        "ActorUsername": {
            "data_type": "Username",
            "description": "The Actor’s username, including domain information when available. For more information, see The User entity.Example: AlbertE",
            "class": "Recommended",
        },
        "User": {"data_type": "", "description": "Alias to ActorUsername", "class": "Alias"},
        "ActorUsernameType": {
            "data_type": "UsernameType",
            "description": "Specifies the type of the user name stored in the ActorUsername field. For more information, and list of allowed values, see UsernameType in the Schema Overview article. Example: Windows",
            "class": "Conditional",
        },
        "ActorUserType": {
            "data_type": "UserType",
            "description": "The type of the Actor. For more information, and  list of allowed values, see UserType in the Schema Overview article.For example: Guest",
            "class": "Optional",
        },
        "ActorOriginalUserType": {
            "data_type": "UserType",
            "description": "The user type as reported by the reporting device.",
            "class": "Optional",
        },
        "ActorSessionId": {
            "data_type": "String",
            "description": "The unique ID of the sign-in session of the Actor.  Example: 102pTUgC3p8RIqHvzxLCHnFlg",
            "class": "Optional",
        },
        "TargetAppId": {
            "data_type": "String",
            "description": "The ID of the application to which the event applies, including a process, browser, or service. Example: 89162",
            "class": "Optional",
        },
        "TargetAppName": {
            "data_type": "String",
            "description": "The name of the application to which event applies, including a service, a URL, or a SaaS application. Example: Exchange 365",
            "class": "Optional",
        },
        "Application": {"data_type": "", "description": "Alias to TargetAppName", "class": "Alias"},
        "TargetAppType": {
            "data_type": "AppType",
            "description": "The type of the application authorizing on behalf of the Actor. For more information, and allowed list of values, see AppType in the Schema Overview article.",
            "class": "Optional",
        },
        "TargetUrl": {
            "data_type": "URL",
            "description": "The URL associated with the target application. Example: https://console.aws.amazon.com/console/home?fromtb=true&hashArgs=%23&isauthcode=true&nc2=h_ct&src=header-signin&state=hashArgsFromTB_us-east-1_7596bc16c83d260b",
            "class": "Optional",
        },
        "Dst": {
            "data_type": "String",
            "description": "A unique identifier of the authentication target. This field may alias the TargerDvcId, TargetHostname, TargetIpAddr, TargetAppId, or TargetAppName fields. Example: 192.168.12.1",
            "class": "Alias",
        },
        "TargetHostname": {
            "data_type": "Hostname",
            "description": "The target device hostname, excluding domain information.Example: DESKTOP-1282V4D",
            "class": "Recommended",
        },
        "TargetDomain": {
            "data_type": "String",
            "description": "The domain of the target device.Example: Contoso",
            "class": "Recommended",
        },
        "TargetDomainType": {
            "data_type": "Enumerated",
            "description": "The type of TargetDomain. For a list of allowed values and further information, refer to DomainType in the Schema Overview article.Required if TargetDomain is used.",
            "class": "Conditional",
        },
        "TargetFQDN": {
            "data_type": "String",
            "description": "The target device hostname, including domain information when available. Example: Contoso\\DESKTOP-1282V4D Note: This field supports both traditional FQDN format and Windows domain\\hostname format. The TargetDomainType reflects the format used.",
            "class": "Optional",
        },
        "TargetDescription": {
            "data_type": "String",
            "description": "A descriptive text associated with the device. For example: Primary Domain Controller.",
            "class": "Optional",
        },
        "TargetDvcId": {
            "data_type": "String",
            "description": "The ID of the target device. If multiple IDs are available, use the most important one, and store the others in the fields TargetDvc<DvcIdType>. Example: ac7e9755-8eae-4ffc-8a02-50ed7a2216c3",
            "class": "Optional",
        },
        "TargetDvcScopeId": {
            "data_type": "String",
            "description": "The cloud platform scope ID the device belongs to. TargetDvcScopeId map to a subscription ID on Azure and to an account ID on AWS.",
            "class": "Optional",
        },
        "TargetDvcScope": {
            "data_type": "String",
            "description": "The cloud platform scope the device belongs to. TargetDvcScope map to a subscription ID on Azure and to an account ID on AWS.",
            "class": "Optional",
        },
        "TargetDvcIdType": {
            "data_type": "Enumerated",
            "description": "The type of TargetDvcId. For a list of allowed values and further information, refer to DvcIdType in the Schema Overview article. Required if TargetDeviceId is used.",
            "class": "Conditional",
        },
        "TargetDeviceType": {
            "data_type": "Enumerated",
            "description": "The type of the target device.  For a list of allowed values and further information, refer to DeviceType in the Schema Overview article.",
            "class": "Optional",
        },
        "TargetIpAddr": {
            "data_type": "IP Address",
            "description": "The IP address of the target device. Example: 2.2.2.2",
            "class": "Optional",
        },
        "TargetDvcOs": {
            "data_type": "String",
            "description": "The OS of the target device. Example: Windows 10",
            "class": "Optional",
        },
        "TargetPortNumber": {
            "data_type": "Integer",
            "description": "The port of the target device.",
            "class": "Optional",
        },
        "ActingAppId": {
            "data_type": "String",
            "description": "The ID of the application that initiated the activity reported, including a process, browser, or service. For example: 0x12ae8",
            "class": "Optional",
        },
        "ActiveAppName": {
            "data_type": "String",
            "description": "The name of the application that initiated the activity reported, including a service, a URL, or a SaaS application. For example: C:\\Windows\\System32\\svchost.exe",
            "class": "Optional",
        },
        "ActingAppType": {
            "data_type": "AppType",
            "description": "The type of acting application. For more information, and allowed list of values, see AppType in the Schema Overview article.",
            "class": "Optional",
        },
        "HttpUserAgent": {
            "data_type": "String",
            "description": "When authentication is performed over HTTP or HTTPS, this field's value is the user_agent HTTP header provided by the acting application when performing the authentication.For example: Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1",
            "class": "Optional",
        },
        "Src": {
            "data_type": "String",
            "description": "A unique identifier of the source device. This field might alias the SrcDvcId, SrcHostname, or SrcIpAddr fields. Example: 192.168.12.1",
            "class": "Alias",
        },
        "SrcIpAddr": {
            "data_type": "IP address",
            "description": "The IP address from which the connection or session originated. Example: 77.138.103.108",
            "class": "Recommended",
        },
        "IpAddr": {
            "data_type": "",
            "description": "Alias to SrcIpAddr, or to TargetIpAddr if SrcIpAddr is not provided.",
            "class": "Alias",
        },
        "SrcPortNumber": {
            "data_type": "Integer",
            "description": "The IP port from which the connection originated. Might not be relevant for a session comprising multiple connections.Example: 2335",
            "class": "Optional",
        },
        "SrcHostname": {
            "data_type": "Hostname",
            "description": "The source device hostname, excluding domain information. If no device name is available, store the relevant IP address in this field.Example: DESKTOP-1282V4D",
            "class": "Recommended",
        },
        "SrcDomain": {
            "data_type": "String",
            "description": "The domain of the source device.Example: Contoso",
            "class": "Recommended",
        },
        "SrcDomainType": {
            "data_type": "DomainType",
            "description": "The type of SrcDomain. For a list of allowed values and further information, refer to DomainType in the Schema Overview article.Required if SrcDomain is used.",
            "class": "Conditional",
        },
        "SrcFQDN": {
            "data_type": "String",
            "description": "The source device hostname, including domain information when available. Note: This field supports both traditional FQDN format and Windows domain\\hostname format. The SrcDomainType field reflects the format used. Example: Contoso\\DESKTOP-1282V4D",
            "class": "Optional",
        },
        "SrcDescription": {
            "data_type": "String",
            "description": "A descriptive text associated with the device. For example: Primary Domain Controller.",
            "class": "Optional",
        },
        "SrcDvcId": {
            "data_type": "String",
            "description": "The ID of the source device. If multiple IDs are available, use the most important one, and store the others in the fields SrcDvc<DvcIdType>.Example: ac7e9755-8eae-4ffc-8a02-50ed7a2216c3",
            "class": "Optional",
        },
        "SrcDvcScopeId": {
            "data_type": "String",
            "description": "The cloud platform scope ID the device belongs to. SrcDvcScopeId map to a subscription ID on Azure and to an account ID on AWS.",
            "class": "Optional",
        },
        "SrcDvcScope": {
            "data_type": "String",
            "description": "The cloud platform scope the device belongs to. SrcDvcScope map to a subscription ID on Azure and to an account ID on AWS.",
            "class": "Optional",
        },
        "SrcDvcIdType": {
            "data_type": "DvcIdType",
            "description": "The type of SrcDvcId. For a list of allowed values and further information, refer to DvcIdType in the Schema Overview article. Note: This field is required if SrcDvcId is used.",
            "class": "Conditional",
        },
        "SrcDeviceType": {
            "data_type": "DeviceType",
            "description": "The type of the source device. For a list of allowed values and further information, refer to DeviceType in the Schema Overview article.",
            "class": "Optional",
        },
        "SrcSubscriptionId": {
            "data_type": "String",
            "description": "The cloud platform subscription ID the source device belongs to. SrcSubscriptionId map to a subscription ID on Azure and to an account ID on AWS.",
            "class": "Optional",
        },
        "SrcGeoCountry": {
            "data_type": "Country",
            "description": "The country associated with the source IP address.Example: USA",
            "class": "Optional",
        },
        "SrcGeoRegion": {
            "data_type": "Region",
            "description": "The region within a country associated with the source IP address.Example: Vermont",
            "class": "Optional",
        },
        "SrcGeoCity": {
            "data_type": "City",
            "description": "The city associated with the source IP address.Example: Burlington",
            "class": "Optional",
        },
        "SrcGeoLatitude": {
            "data_type": "Latitude",
            "description": "The latitude of the geographical coordinate associated with the source IP address.Example: 44.475833",
            "class": "Optional",
        },
        "SrcGeoLongitude": {
            "data_type": "Longitude",
            "description": "The longitude of the geographical coordinate associated with the source IP address.Example: 73.211944",
            "class": "Optional",
        },
        "RuleName": {
            "data_type": "String",
            "description": "The name or ID of the rule by associated with the inspection results.",
            "class": "Optional",
        },
        "RuleNumber": {
            "data_type": "Integer",
            "description": "The number of the rule associated with the inspection results.",
            "class": "Optional",
        },
        "Rule": {
            "data_type": "String",
            "description": "Either the value of RuleName or the value of RuleNumber. If the value of RuleNumber is used, the type should be converted to string.",
            "class": "Alias",
        },
        "ThreatId": {
            "data_type": "String",
            "description": "The ID of the threat or malware identified in the audit activity.",
            "class": "Optional",
        },
        "ThreatName": {
            "data_type": "String",
            "description": "The name of the threat or malware identified in the audit activity.",
            "class": "Optional",
        },
        "ThreatCategory": {
            "data_type": "String",
            "description": "The category of the threat or malware identified in audit file activity.",
            "class": "Optional",
        },
        "ThreatRiskLevel": {
            "data_type": "Integer",
            "description": "The risk level associated with the identified threat. The level should be a number between 0 and 100.Note: The value might be provided in the source record by using a different scale, which should be normalized to this scale. The original value should be stored in ThreatRiskLevelOriginal.",
            "class": "Optional",
        },
        "ThreatOriginalRiskLevel": {
            "data_type": "String",
            "description": "The risk level as reported by the reporting device.",
            "class": "Optional",
        },
        "ThreatConfidence": {
            "data_type": "Integer",
            "description": "The confidence level of the threat identified, normalized to a value between 0 and a 100.",
            "class": "Optional",
        },
        "ThreatOriginalConfidence": {
            "data_type": "String",
            "description": "The original confidence level of the threat identified, as reported by the reporting device.",
            "class": "Optional",
        },
        "ThreatIsActive": {
            "data_type": "Boolean",
            "description": "True if the threat identified is considered an active threat.",
            "class": "Optional",
        },
        "ThreatFirstReportedTime": {
            "data_type": "datetime",
            "description": "The first time the IP address or domain were identified as a threat.",
            "class": "Optional",
        },
        "ThreatLastReportedTime": {
            "data_type": "datetime",
            "description": "The last time the IP address or domain were identified as a threat.",
            "class": "Optional",
        },
        "ThreatIpAddr": {
            "data_type": "IP Address",
            "description": "An IP address for which a threat was identified. The field ThreatField contains the name of the field ThreatIpAddr represents.",
            "class": "Optional",
        },
        "ThreatField": {
            "data_type": "Enumerated",
            "description": "The field for which a threat was identified. The value is either SrcIpAddr or TargetIpAddr.",
            "class": "Optional",
        },
    },
    "imAuthentication": {
        "EventType": {
            "data_type": "Enumerated",
            "description": "Describes the operation reported by the record. For Authentication records, supported values include: - Logon - Logoff- Elevate",
            "class": "Mandatory",
        },
        "EventResultDetails": {
            "data_type": "String",
            "description": "The details associated with the event result. This field is typically populated when the result is a failure.Allowed values include:  - No such user or password. This value should be used also when the original event reports that there is no such user, without reference to a password. - No such user - Incorrect password - Incorrect key-\tAccount expired-\tPassword expired-\tUser locked-\tUser disabled - Logon violates policy. This value should be used when the original event reports, for example: MFA required, logon outside of working hours, conditional access restrictions, or too frequent attempts.-\tSession expired-\tOtherThe value may be provided in the source record using different terms, which should be normalized to these values. The original value should be stored in the field EventOriginalResultDetails",
            "class": "Recommended",
        },
        "EventSubType": {
            "data_type": "String",
            "description": "The sign-in type. Allowed values include: - System - Interactive - RemoteInteractive - Service - RemoteService - Remote - Use when the type of remote sign-in is unknown. - AssumeRole - Typically used when the event type is Elevate. The value may be provided in the source record using different terms, which should be normalized to these values. The original value should be stored in the field EventOriginalSubType.",
            "class": "Optional",
        },
        "EventSchemaVersion": {
            "data_type": "String",
            "description": "The version of the schema. The version of the schema documented here is 0.1.3",
            "class": "Mandatory",
        },
        "EventSchema": {
            "data_type": "String",
            "description": "The name of the schema documented here is Authentication.",
            "class": "Mandatory",
        },
        "Dvc fields": {
            "data_type": "-",
            "description": "For authentication events, device fields refer to the system reporting the event.",
            "class": "-",
        },
        "LogonMethod": {
            "data_type": "String",
            "description": "The method used to perform authentication. Examples: Username & Password, PKI",
            "class": "Optional",
        },
        "LogonProtocol": {
            "data_type": "String",
            "description": "The protocol used to perform authentication. Example: NTLM",
            "class": "Optional",
        },
        "ActorUserId": {
            "data_type": "String",
            "description": "A machine-readable, alphanumeric, unique representation of the Actor. For more information, and for alternative fields for additional IDs, see The User entity.  Example: S-1-12-1-4141952679-1282074057-627758481-2916039507",
            "class": "Optional",
        },
        "ActorScope": {
            "data_type": "String",
            "description": "The scope, such as Microsoft Entra tenant, in which ActorUserId and ActorUsername are defined. or more information and list of allowed values, see UserScope in the Schema Overview article.",
            "class": "Optional",
        },
        "ActorScopeId": {
            "data_type": "String",
            "description": "The scope ID, such as Microsoft Entra Directory ID, in which ActorUserId and ActorUsername are defined. for more information and list of allowed values, see UserScopeId in the Schema Overview article.",
            "class": "Optional",
        },
        "ActorUserIdType": {
            "data_type": "UserIdType",
            "description": "The type of the ID stored in the ActorUserId field. For more information and list of allowed values, see UserIdType in the Schema Overview article.",
            "class": "Conditional",
        },
        "ActorUsername": {
            "data_type": "Username",
            "description": "The Actor’s username, including domain information when available. For more information, see The User entity.Example: AlbertE",
            "class": "Optional",
        },
        "ActorUsernameType": {
            "data_type": "UsernameType",
            "description": "Specifies the type of the user name stored in the ActorUsername field. For more information, and list of allowed values, see UsernameType in the Schema Overview article. Example: Windows",
            "class": "Conditional",
        },
        "ActorUserType": {
            "data_type": "UserType",
            "description": "The type of the Actor. For more information, and  list of allowed values, see UserType in the Schema Overview article.For example: Guest",
            "class": "Optional",
        },
        "ActorOriginalUserType": {
            "data_type": "UserType",
            "description": "The user type as reported by the reporting device.",
            "class": "Optional",
        },
        "ActorSessionId": {
            "data_type": "String",
            "description": "The unique ID of the sign-in session of the Actor.  Example: 102pTUgC3p8RIqHvzxLCHnFlg",
            "class": "Optional",
        },
        "ActingAppId": {
            "data_type": "String",
            "description": "The ID of the application authorizing on behalf of the actor, including a process, browser, or service. For example: 0x12ae8",
            "class": "Optional",
        },
        "ActingAppName": {
            "data_type": "String",
            "description": "The name of the application authorizing on behalf of the actor, including a process, browser, or service. For example: C:\\Windows\\System32\\svchost.exe",
            "class": "Optional",
        },
        "ActingAppType": {
            "data_type": "AppType",
            "description": "The type of acting application. For more information, and allowed list of values, see AppType in the Schema Overview article.",
            "class": "Optional",
        },
        "HttpUserAgent": {
            "data_type": "String",
            "description": "When authentication is performed over HTTP or HTTPS, this field's value is the user_agent HTTP header provided by the acting application when performing the authentication.For example: Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1",
            "class": "Optional",
        },
        "TargetUserId": {
            "data_type": "UserId",
            "description": "A machine-readable, alphanumeric, unique representation of the target user. For more information, and for alternative fields for additional IDs, see The User entity.   Example: 00urjk4znu3BcncfY0h7",
            "class": "Optional",
        },
        "TargetUserScope": {
            "data_type": "String",
            "description": "The scope, such as Microsoft Entra tenant, in which TargetUserId and TargetUsername are defined. or more information and list of allowed values, see UserScope in the Schema Overview article.",
            "class": "Optional",
        },
        "TargetUserScopeId": {
            "data_type": "String",
            "description": "The scope ID, such as Microsoft Entra Directory ID, in which TargetUserId and TargetUsername are defined. for more information and list of allowed values, see UserScopeId in the Schema Overview article.",
            "class": "Optional",
        },
        "TargetUserIdType": {
            "data_type": "UserIdType",
            "description": "The type of the user ID stored in the TargetUserId field. For more information and list of allowed values, see UserIdType in the Schema Overview article.             Example:  SID",
            "class": "Conditional",
        },
        "TargetUsername": {
            "data_type": "Username",
            "description": "The target user username, including domain information when available. For more information, see The User entity.  Example:   MarieC",
            "class": "Optional",
        },
        "TargetUsernameType": {
            "data_type": "UsernameType",
            "description": "Specifies the type of the username stored in the TargetUsername field. For more information and list of allowed values, see UsernameType in the Schema Overview article.",
            "class": "Conditional",
        },
        "TargetUserType": {
            "data_type": "UserType",
            "description": "The type of the Target user. For more information, and  list of allowed values, see UserType in the Schema Overview article. For example: Member",
            "class": "Optional",
        },
        "TargetSessionId": {
            "data_type": "String",
            "description": "The sign-in session identifier of the TargetUser on the source device.",
            "class": "Optional",
        },
        "TargetOriginalUserType": {
            "data_type": "UserType",
            "description": "The user type as reported by the reporting device.",
            "class": "Optional",
        },
        "User": {
            "data_type": "Username",
            "description": "Alias to the TargetUsername or to the TargetUserId if TargetUsername is not defined. Example: CONTOSO\\dadmin",
            "class": "Alias",
        },
        "Src": {
            "data_type": "String",
            "description": "A unique identifier of the source device. This field may alias the SrcDvcId, SrcHostname, or SrcIpAddr fields. Example: 192.168.12.1",
            "class": "Recommended",
        },
        "SrcDvcId": {
            "data_type": "String",
            "description": "The ID of the source device. If multiple IDs are available, use the most important one, and store the others in the fields SrcDvc<DvcIdType>.Example: ac7e9755-8eae-4ffc-8a02-50ed7a2216c3",
            "class": "Optional",
        },
        "SrcDvcScopeId": {
            "data_type": "String",
            "description": "The cloud platform scope ID the device belongs to. SrcDvcScopeId map to a subscription ID on Azure and to an account ID on AWS.",
            "class": "Optional",
        },
        "SrcDvcScope": {
            "data_type": "String",
            "description": "The cloud platform scope the device belongs to. SrcDvcScope map to a subscription ID on Azure and to an account ID on AWS.",
            "class": "Optional",
        },
        "SrcDvcIdType": {
            "data_type": "DvcIdType",
            "description": "The type of SrcDvcId. For a list of allowed values and further information refer to DvcIdType in the Schema Overview article. Note: This field is required if SrcDvcId is used.",
            "class": "Conditional",
        },
        "SrcDeviceType": {
            "data_type": "DeviceType",
            "description": "The type of the source device. For a list of allowed values and further information refer to DeviceType in the Schema Overview article.",
            "class": "Optional",
        },
        "SrcHostname": {
            "data_type": "Hostname",
            "description": "The source device hostname, excluding domain information. If no device name is available, store the relevant IP address in this field. Example: DESKTOP-1282V4D",
            "class": "Recommended",
        },
        "SrcDomain": {
            "data_type": "String",
            "description": "The domain of the source device.Example: Contoso",
            "class": "Recommended",
        },
        "SrcDomainType": {
            "data_type": "DomainType",
            "description": "The type of SrcDomain. For a list of allowed values and further information refer to DomainType in the Schema Overview article.Required if SrcDomain is used.",
            "class": "Conditional",
        },
        "SrcFQDN": {
            "data_type": "String",
            "description": "The source device hostname, including domain information when available. Note: This field supports both traditional FQDN format and Windows domain\\hostname format. The SrcDomainType field reflects the format used. Example: Contoso\\DESKTOP-1282V4D",
            "class": "Optional",
        },
        "SrcDescription": {
            "data_type": "String",
            "description": "A descriptive text associated with the device. For example: Primary Domain Controller.",
            "class": "Optional",
        },
        "SrcIpAddr": {
            "data_type": "IP Address",
            "description": "The IP address of the source device. Example: 2.2.2.2",
            "class": "Optional",
        },
        "SrcPortNumber": {
            "data_type": "Integer",
            "description": "The IP port from which the connection originated.Example: 2335",
            "class": "Optional",
        },
        "SrcDvcOs": {
            "data_type": "String",
            "description": "The OS of the source device. Example: Windows 10",
            "class": "Optional",
        },
        "IpAddr": {"data_type": "", "description": "Alias to SrcIpAddr", "class": "Alias"},
        "SrcIsp": {
            "data_type": "String",
            "description": "The Internet Service Provider (ISP) used by the source device to connect to the internet. Example: corpconnect",
            "class": "Optional",
        },
        "SrcGeoCountry": {
            "data_type": "Country",
            "description": "Example: Canada For more information, see Logical types.",
            "class": "Optional",
        },
        "SrcGeoCity": {
            "data_type": "City",
            "description": "Example: Montreal For more information, see Logical types.",
            "class": "Optional",
        },
        "SrcGeoRegion": {
            "data_type": "Region",
            "description": "Example: Quebec For more information, see Logical types.",
            "class": "Optional",
        },
        "SrcGeoLongtitude": {
            "data_type": "Longitude",
            "description": "Example: -73.614830 For more information, see Logical types.",
            "class": "Optional",
        },
        "SrcGeoLatitude": {
            "data_type": "Latitude",
            "description": "Example: 45.505918 For more information, see Logical types.",
            "class": "Optional",
        },
        "SrcRiskLevel": {
            "data_type": "Integer",
            "description": "The risk level associated with the source. The value should be adjusted to a range of 0 to 100, with 0 for benign and 100 for a high risk.Example: 90",
            "class": "Optional",
        },
        "SrcOriginalRiskLevel": {
            "data_type": "Integer",
            "description": "The risk level associated with the source, as reported by the reporting device. Example: Suspicious",
            "class": "Optional",
        },
        "TargetAppId": {
            "data_type": "String",
            "description": "The ID of the application to which the authorization is required, often assigned by the reporting device. Example: 89162",
            "class": "Optional",
        },
        "TargetAppName": {
            "data_type": "String",
            "description": "The name of the application to which the authorization is required, including a service, a URL, or a SaaS application. Example: Saleforce",
            "class": "Optional",
        },
        "TargetAppType": {
            "data_type": "AppType",
            "description": "The type of the application authorizing on behalf of the Actor. For more information, and allowed list of values, see AppType in the Schema Overview article.",
            "class": "Optional",
        },
        "TargetUrl": {
            "data_type": "URL",
            "description": "The URL associated with the target application. Example: https://console.aws.amazon.com/console/home?fromtb=true&hashArgs=%23&isauthcode=true&nc2=h_ct&src=header-signin&state=hashArgsFromTB_us-east-1_7596bc16c83d260b",
            "class": "Optional",
        },
        "LogonTarget": {
            "data_type": "",
            "description": "Alias to either TargetAppName, TargetUrl, or TargetHostname, whichever field best describes the authentication target.",
            "class": "Alias",
        },
        "Dst": {
            "data_type": "String",
            "description": "A unique identifier of the authentication target. This field may alias the TargerDvcId, TargetHostname, TargetIpAddr, TargetAppId, or TargetAppName fields. Example: 192.168.12.1",
            "class": "Alias",
        },
        "TargetHostname": {
            "data_type": "Hostname",
            "description": "The target device hostname, excluding domain information.Example: DESKTOP-1282V4D",
            "class": "Recommended",
        },
        "TargetDomain": {
            "data_type": "String",
            "description": "The domain of the target device.Example: Contoso",
            "class": "Recommended",
        },
        "TargetDomainType": {
            "data_type": "Enumerated",
            "description": "The type of TargetDomain. For a list of allowed values and further information refer to DomainType in the Schema Overview article.Required if TargetDomain is used.",
            "class": "Conditional",
        },
        "TargetFQDN": {
            "data_type": "String",
            "description": "The target device hostname, including domain information when available. Example: Contoso\\DESKTOP-1282V4D Note: This field supports both traditional FQDN format and Windows domain\\hostname format. The TargetDomainType reflects the format used.",
            "class": "Optional",
        },
        "TargetDescription": {
            "data_type": "String",
            "description": "A descriptive text associated with the device. For example: Primary Domain Controller.",
            "class": "Optional",
        },
        "TargetDvcId": {
            "data_type": "String",
            "description": "The ID of the target device. If multiple IDs are available, use the most important one, and store the others in the fields TargetDvc<DvcIdType>. Example: ac7e9755-8eae-4ffc-8a02-50ed7a2216c3",
            "class": "Optional",
        },
        "TargetDvcScopeId": {
            "data_type": "String",
            "description": "The cloud platform scope ID the device belongs to. TargetDvcScopeId map to a subscription ID on Azure and to an account ID on AWS.",
            "class": "Optional",
        },
        "TargerDvcScope": {
            "data_type": "String",
            "description": "The cloud platform scope the device belongs to. TargetDvcScope map to a subscription ID on Azure and to an account ID on AWS.",
            "class": "Optional",
        },
        "TargetDvcIdType": {
            "data_type": "Enumerated",
            "description": "The type of TargetDvcId. For a list of allowed values and further information refer to DvcIdType in the Schema Overview article. Required if TargetDeviceId is used.",
            "class": "Conditional",
        },
        "TargetDeviceType": {
            "data_type": "Enumerated",
            "description": "The type of the target device.  For a list of allowed values and further information refer to DeviceType in the Schema Overview article.",
            "class": "Optional",
        },
        "TargetIpAddr": {
            "data_type": "IP Address",
            "description": "The IP address of the target device. Example: 2.2.2.2",
            "class": "Optional",
        },
        "TargetDvcOs": {
            "data_type": "String",
            "description": "The OS of the target device. Example: Windows 10",
            "class": "Optional",
        },
        "TargetPortNumber": {
            "data_type": "Integer",
            "description": "The port of the target device.",
            "class": "Optional",
        },
        "TargetGeoCountry": {
            "data_type": "Country",
            "description": "The country associated with the target IP address.Example: USA",
            "class": "Optional",
        },
        "TargetGeoRegion": {
            "data_type": "Region",
            "description": "The region associated with the target IP address.Example: Vermont",
            "class": "Optional",
        },
        "TargetGeoCity": {
            "data_type": "City",
            "description": "The city associated with the target IP address.Example: Burlington",
            "class": "Optional",
        },
        "TargetGeoLatitude": {
            "data_type": "Latitude",
            "description": "The latitude of the geographical coordinate associated with the target IP address.Example: 44.475833",
            "class": "Optional",
        },
        "TargetGeoLongitude": {
            "data_type": "Longitude",
            "description": "The longitude of the geographical coordinate associated with the target IP address.Example: 73.211944",
            "class": "Optional",
        },
        "TargetRiskLevel": {
            "data_type": "Integer",
            "description": "The risk level associated with the target. The value should be adjusted to a range of 0 to 100, with 0 for benign and 100 for a high risk.Example: 90",
            "class": "Optional",
        },
        "TargetOriginalRiskLevel": {
            "data_type": "Integer",
            "description": "The risk level associated with the target, as reported by the reporting device. Example: Suspicious",
            "class": "Optional",
        },
        "RuleName": {
            "data_type": "String",
            "description": "The name or ID of the rule by associated with the inspection results.",
            "class": "Optional",
        },
        "RuleNumber": {
            "data_type": "Integer",
            "description": "The number of the rule associated with the inspection results.",
            "class": "Optional",
        },
        "Rule": {
            "data_type": "String",
            "description": "Either the value of RuleName or the value of RuleNumber. If the value of RuleNumber is used, the type should be converted to string.",
            "class": "Alias",
        },
        "ThreatId": {
            "data_type": "String",
            "description": "The ID of the threat or malware identified in the audit activity.",
            "class": "Optional",
        },
        "ThreatName": {
            "data_type": "String",
            "description": "The name of the threat or malware identified in the audit activity.",
            "class": "Optional",
        },
        "ThreatCategory": {
            "data_type": "String",
            "description": "The category of the threat or malware identified in audit file activity.",
            "class": "Optional",
        },
        "ThreatRiskLevel": {
            "data_type": "Integer",
            "description": "The risk level associated with the identified threat. The level should be a number between 0 and 100.Note: The value might be provided in the source record by using a different scale, which should be normalized to this scale. The original value should be stored in ThreatRiskLevelOriginal.",
            "class": "Optional",
        },
        "ThreatOriginalRiskLevel": {
            "data_type": "String",
            "description": "The risk level as reported by the reporting device.",
            "class": "Optional",
        },
        "ThreatConfidence": {
            "data_type": "Integer",
            "description": "The confidence level of the threat identified, normalized to a value between 0 and a 100.",
            "class": "Optional",
        },
        "ThreatOriginalConfidence": {
            "data_type": "String",
            "description": "The original confidence level of the threat identified, as reported by the reporting device.",
            "class": "Optional",
        },
        "ThreatIsActive": {
            "data_type": "Boolean",
            "description": "True if the threat identified is considered an active threat.",
            "class": "Optional",
        },
        "ThreatFirstReportedTime": {
            "data_type": "datetime",
            "description": "The first time the IP address or domain were identified as a threat.",
            "class": "Optional",
        },
        "ThreatLastReportedTime": {
            "data_type": "datetime",
            "description": "The last time the IP address or domain were identified as a threat.",
            "class": "Optional",
        },
        "ThreatIpAddr": {
            "data_type": "IP Address",
            "description": "An IP address for which a threat was identified. The field ThreatField contains the name of the field ThreatIpAddr represents.",
            "class": "Optional",
        },
        "ThreatField": {
            "data_type": "Enumerated",
            "description": "The field for which a threat was identified. The value is either SrcIpAddr or TargetIpAddr.",
            "class": "Optional",
        },
    },
    "_Im_Dns": {
        "EventType": {
            "data_type": "Enumerated",
            "description": "Indicates the operation reported by the record.  For DNS records, this value would be the DNS op code. Example: Query",
            "class": "Mandatory",
        },
        "EventSubType": {
            "data_type": "Enumerated",
            "description": "Either request or response. For most sources, only the responses are logged, and therefore the value is often response.",
            "class": "Optional",
        },
        "EventResultDetails": {
            "data_type": "Enumerated",
            "description": "For DNS events, this field provides the DNS response code. Notes:- IANA doesn't define the case for the values, so analytics must normalize the case. - If the source provides only a numerical response code and not a response code name, the parser must include a lookup table to enrich with this value. - If this record represents a request and not a response, set to NA. Example: NXDOMAIN",
            "class": "Mandatory",
        },
        "EventSchemaVersion": {
            "data_type": "String",
            "description": "The version of the schema documented here is 0.1.7.",
            "class": "Mandatory",
        },
        "EventSchema": {
            "data_type": "String",
            "description": "The name of the schema documented here is Dns.",
            "class": "Mandatory",
        },
        "Dvc fields": {
            "data_type": "-",
            "description": "For DNS events, device fields refer to the system that reports the DNS event.",
            "class": "-",
        },
        "Src": {
            "data_type": "String",
            "description": "A unique identifier of the source device. This field can alias the SrcDvcId, SrcHostname, or SrcIpAddr fields. Example: 192.168.12.1",
            "class": "Alias",
        },
        "SrcIpAddr": {
            "data_type": "IP Address",
            "description": "The IP address of the client that sent the DNS request. For a recursive DNS request, this value would typically be the reporting device, and in most cases set to 127.0.0.1. Example: 192.168.12.1",
            "class": "Recommended",
        },
        "SrcPortNumber": {
            "data_type": "Integer",
            "description": "Source port of the DNS query.Example: 54312",
            "class": "Optional",
        },
        "IpAddr": {"data_type": "", "description": "Alias to SrcIpAddr", "class": "Alias"},
        "SrcGeoCountry": {
            "data_type": "Country",
            "description": "The country associated with the source IP address.Example: USA",
            "class": "Optional",
        },
        "SrcGeoRegion": {
            "data_type": "Region",
            "description": "The region associated with the source IP address.Example: Vermont",
            "class": "Optional",
        },
        "SrcGeoCity": {
            "data_type": "City",
            "description": "The city associated with the source IP address.Example: Burlington",
            "class": "Optional",
        },
        "SrcGeoLatitude": {
            "data_type": "Latitude",
            "description": "The latitude of the geographical coordinate associated with the source IP address.Example: 44.475833",
            "class": "Optional",
        },
        "SrcGeoLongitude": {
            "data_type": "Longitude",
            "description": "The longitude of the geographical coordinate associated with the source IP address.Example: 73.211944",
            "class": "Optional",
        },
        "SrcRiskLevel": {
            "data_type": "Integer",
            "description": "The risk level associated with the source. The value should be adjusted to a range of 0 to 100, with 0 for benign and 100 for a high risk.Example: 90",
            "class": "Optional",
        },
        "SrcOriginalRiskLevel": {
            "data_type": "Integer",
            "description": "The risk level associated with the source, as reported by the reporting device. Example: Suspicious",
            "class": "Optional",
        },
        "SrcHostname": {
            "data_type": "String",
            "description": "The source device hostname, excluding domain information.Example: DESKTOP-1282V4D",
            "class": "Recommended",
        },
        "Hostname": {"data_type": "", "description": "Alias to SrcHostname", "class": "Alias"},
        "SrcDomain": {
            "data_type": "String",
            "description": "The domain of the source device.Example: Contoso",
            "class": "Recommended",
        },
        "SrcDomainType": {
            "data_type": "Enumerated",
            "description": "The type of  SrcDomain, if known. Possible values include:- Windows (such as: contoso)- FQDN (such as: microsoft.com)Required if SrcDomain is used.",
            "class": "Conditional",
        },
        "SrcFQDN": {
            "data_type": "String",
            "description": "The source device hostname, including domain information when available. Note: This field supports both traditional FQDN format and Windows domain\\hostname format. The SrcDomainType field reflects the format used. Example: Contoso\\DESKTOP-1282V4D",
            "class": "Optional",
        },
        "SrcDvcId": {
            "data_type": "String",
            "description": "The ID of the source device as reported in the record.For example: ac7e9755-8eae-4ffc-8a02-50ed7a2216c3",
            "class": "Optional",
        },
        "SrcDvcScopeId": {
            "data_type": "String",
            "description": "The cloud platform scope ID the device belongs to. SrcDvcScopeId map to a subscription ID on Azure and to an account ID on AWS.",
            "class": "Optional",
        },
        "SrcDvcScope": {
            "data_type": "String",
            "description": "The cloud platform scope the device belongs to. SrcDvcScope map to a subscription ID on Azure and to an account ID on AWS.",
            "class": "Optional",
        },
        "SrcDvcIdType": {
            "data_type": "Enumerated",
            "description": "The type of SrcDvcId, if known. Possible values include: - AzureResourceId- MDEidIf multiple IDs are available, use the first one from the list, and store the others in the SrcDvcAzureResourceId and SrcDvcMDEid, respectively.Note: This field is required if SrcDvcId is used.",
            "class": "Conditional",
        },
        "SrcDeviceType": {
            "data_type": "Enumerated",
            "description": "The type of the source device. Possible values include:- Computer- Mobile Device- IOT Device- Other",
            "class": "Optional",
        },
        "SrcDescription": {
            "data_type": "String",
            "description": "A descriptive text associated with the device. For example: Primary Domain Controller.",
            "class": "Optional",
        },
        "SrcUserId": {
            "data_type": "String",
            "description": "A machine-readable, alphanumeric, unique representation of the source user. For more information, and for alternative fields for additional IDs, see The User entity.  Example: S-1-12-1-4141952679-1282074057-627758481-2916039507",
            "class": "Optional",
        },
        "SrcUserScope": {
            "data_type": "String",
            "description": "The scope, such as Microsoft Entra tenant, in which SrcUserId and SrcUsername are defined. or more information and list of allowed values, see UserScope in the Schema Overview article.",
            "class": "Optional",
        },
        "SrcUserScopeId": {
            "data_type": "String",
            "description": "The scope ID, such as Microsoft Entra Directory ID, in which SrcUserId and SrcUsername are defined. for more information and list of allowed values, see UserScopeId in the Schema Overview article.",
            "class": "Optional",
        },
        "SrcUserIdType": {
            "data_type": "UserIdType",
            "description": "The type of the ID stored in the SrcUserId field. For more information and list of allowed values, see UserIdType in the Schema Overview article.",
            "class": "Conditional",
        },
        "SrcUsername": {
            "data_type": "Username",
            "description": "The source username, including domain information when available. For more information, see The User entity.Example: AlbertE",
            "class": "Optional",
        },
        "SrcUsernameType": {
            "data_type": "UsernameType",
            "description": "Specifies the type of the user name stored in the SrcUsername field. For more information, and list of allowed values, see UsernameType in the Schema Overview article. Example: Windows",
            "class": "Conditional",
        },
        "User": {"data_type": "", "description": "Alias to SrcUsername", "class": "Alias"},
        "SrcUserType": {
            "data_type": "UserType",
            "description": "The type of the source user. For more information, and  list of allowed values, see UserType in the Schema Overview article.For example: Guest",
            "class": "Optional",
        },
        "SrcUserSessionId": {
            "data_type": "String",
            "description": "The unique ID of the sign-in session of the Actor.  Example: 102pTUgC3p8RIqHvzxLCHnFlg",
            "class": "Optional",
        },
        "SrcOriginalUserType": {
            "data_type": "String",
            "description": "The original source user type, if provided by the source.",
            "class": "Optional",
        },
        "SrcProcessName": {
            "data_type": "String",
            "description": "The file name of the process that initiated the DNS request. This name is typically considered to be the process name.  Example: C:\\Windows\\explorer.exe",
            "class": "Optional",
        },
        "Process": {
            "data_type": "",
            "description": "Alias to the SrcProcessName Example: C:\\Windows\\System32\\rundll32.exe",
            "class": "Alias",
        },
        "SrcProcessId": {
            "data_type": "String",
            "description": "The process ID (PID) of the process that initiated the DNS request.Example:  48610176 Note: The type is defined as string to support varying systems, but on Windows and Linux this value must be numeric. If you are using a Windows or Linux machine and used a different type, make sure to convert the values. For example, if you used a hexadecimal value, convert it to a decimal value.",
            "class": "Optional",
        },
        "SrcProcessGuid": {
            "data_type": "String",
            "description": "A generated unique identifier (GUID) of the process that initiated the DNS request.    Example: EF3BD0BD-2B74-60C5-AF5C-010000001E00",
            "class": "Optional",
        },
        "Dst": {
            "data_type": "String",
            "description": "A unique identifier of the server that received the DNS request. This field may alias the DstDvcId, DstHostname, or DstIpAddr fields. Example: 192.168.12.1",
            "class": "Alias",
        },
        "DstIpAddr": {
            "data_type": "IP Address",
            "description": "The IP address of the server that received the DNS request. For a regular DNS request, this value would typically be the reporting device, and in most cases set to 127.0.0.1.Example: 127.0.0.1",
            "class": "Optional",
        },
        "DstGeoCountry": {
            "data_type": "Country",
            "description": "The country associated with the destination IP address. For more information, see Logical types.Example: USA",
            "class": "Optional",
        },
        "DstGeoRegion": {
            "data_type": "Region",
            "description": "The region, or state, associated with the destination IP address. For more information, see Logical types.Example: Vermont",
            "class": "Optional",
        },
        "DstGeoCity": {
            "data_type": "City",
            "description": "The city associated with the destination IP address. For more information, see Logical types.Example: Burlington",
            "class": "Optional",
        },
        "DstGeoLatitude": {
            "data_type": "Latitude",
            "description": "The latitude of the geographical coordinate associated with the destination IP address. For more information, see Logical types.Example: 44.475833",
            "class": "Optional",
        },
        "DstGeoLongitude": {
            "data_type": "Longitude",
            "description": "The longitude of the geographical coordinate associated with the destination IP address. For more information, see Logical types.Example: 73.211944",
            "class": "Optional",
        },
        "DstRiskLevel": {
            "data_type": "Integer",
            "description": "The risk level associated with the destination. The value should be adjusted to a range of 0 to 100, which 0 being benign and 100 being a high risk.Example: 90",
            "class": "Optional",
        },
        "DstOriginalRiskLevel": {
            "data_type": "Integer",
            "description": "The risk level associated with the destination, as reported by the reporting device. Example: Malicious",
            "class": "Optional",
        },
        "DstPortNumber": {
            "data_type": "Integer",
            "description": "Destination Port number.Example: 53",
            "class": "Optional",
        },
        "DstHostname": {
            "data_type": "String",
            "description": "The destination device hostname, excluding domain information. If no device name is available, store the relevant IP address in this field.Example: DESKTOP-1282V4DNote: This value is mandatory if DstIpAddr is specified.",
            "class": "Optional",
        },
        "DstDomain": {
            "data_type": "String",
            "description": "The domain of the destination device.Example: Contoso",
            "class": "Optional",
        },
        "DstDomainType": {
            "data_type": "Enumerated",
            "description": "The type of DstDomain, if known. Possible values include:- Windows (contoso\\mypc)- FQDN (learn.microsoft.com)Required if DstDomain is used.",
            "class": "Conditional",
        },
        "DstFQDN": {
            "data_type": "String",
            "description": "The destination device hostname, including domain information when available. Example: Contoso\\DESKTOP-1282V4D Note: This field supports both traditional FQDN format and Windows domain\\hostname format. The DstDomainType reflects the format used.",
            "class": "Optional",
        },
        "DstDvcId": {
            "data_type": "String",
            "description": "The ID of the destination device as reported in the record.Example: ac7e9755-8eae-4ffc-8a02-50ed7a2216c3",
            "class": "Optional",
        },
        "DstDvcScopeId": {
            "data_type": "String",
            "description": "The cloud platform scope ID the device belongs to. DstDvcScopeId map to a subscription ID on Azure and to an account ID on AWS.",
            "class": "Optional",
        },
        "DstDvcScope": {
            "data_type": "String",
            "description": "The cloud platform scope the device belongs to. DstDvcScope map to a subscription ID on Azure and to an account ID on AWS.",
            "class": "Optional",
        },
        "DstDvcIdType": {
            "data_type": "Enumerated",
            "description": "The type of DstDvcId, if known. Possible values include: - AzureResourceId- MDEidIfIf multiple IDs are available, use the first one from the list above, and store the others in the  DstDvcAzureResourceId or DstDvcMDEid fields, respectively.Required if DstDeviceId is used.",
            "class": "Conditional",
        },
        "DstDeviceType": {
            "data_type": "Enumerated",
            "description": "The type of the destination device. Possible values include:- Computer- Mobile Device- IOT Device- Other",
            "class": "Optional",
        },
        "DstDescription": {
            "data_type": "String",
            "description": "A descriptive text associated with the device. For example: Primary Domain Controller.",
            "class": "Optional",
        },
        "DnsQuery": {
            "data_type": "String",
            "description": "The domain that the request tries to resolve. Notes: - Some sources send valid FQDN queries in a different format. For example, in the DNS protocol itself, the query includes a dot (.) at the end, which must be removed.- While the DNS protocol limits the type of value in this field to an FQDN, most DNS servers allow any value, and this field is therefore not limited to FQDN values only. Most notably, DNS tunneling attacks may use invalid FQDN values in the query field.- While the DNS protocol allows for multiple queries in a single request, this scenario is rare, if it's found at all. If the request has multiple queries, store the first one in this field, and then and optionally keep the rest in the AdditionalFields field.Example: www.malicious.com",
            "class": "Mandatory",
        },
        "Domain": {"data_type": "", "description": "Alias to DnsQuery.", "class": "Alias"},
        "DnsQueryType": {
            "data_type": "Integer",
            "description": "The DNS Resource Record Type codes. Example: 28",
            "class": "Optional",
        },
        "DnsQueryTypeName": {
            "data_type": "Enumerated",
            "description": "The DNS Resource Record Type names. Notes: - IANA doesn't define the case for the values, so analytics must normalize the case as needed.- The value ANY is supported for the response code 255. - The value TYPExxxx is supported for unmapped response codes, where xxxx is the numerical value of the response code, as reported by the BIND DNS server. -If the source provides only a numerical query type code and not a query type name, the parser must include a lookup table to enrich with this value.Example: AAAA",
            "class": "Recommended",
        },
        "DnsResponseName": {
            "data_type": "String",
            "description": "The content of the response, as included in the record.  The DNS response data is inconsistent across reporting devices, is complex to parse, and has less value for source-agnostic analytics. Therefore the information model doesn't require parsing and normalization, and Microsoft Sentinel uses an auxiliary function to provide response information. For more information, see Handling DNS response.",
            "class": "Optional",
        },
        "DnsResponseCodeName": {"data_type": "", "description": "Alias to EventResultDetails", "class": "Alias"},
        "DnsResponseCode": {
            "data_type": "Integer",
            "description": "The DNS numerical response code. Example: 3",
            "class": "Optional",
        },
        "TransactionIdHex": {
            "data_type": "String",
            "description": "The DNS query unique ID as assigned by the DNS client, in hexadecimal format. Note that this value is part of the DNS protocol and different from DnsSessionId, the network layer session ID, typically assigned by the reporting device.",
            "class": "Recommended",
        },
        "NetworkProtocol": {
            "data_type": "Enumerated",
            "description": "The transport protocol used by the network resolution event. The value can be UDP or TCP, and is most commonly set to UDP for DNS. Example: UDP",
            "class": "Optional",
        },
        "NetworkProtocolVersion": {
            "data_type": "Enumerated",
            "description": "The version of NetworkProtocol. When using it to distinguish between IP version, use the values IPv4 and IPv6.",
            "class": "Optional",
        },
        "DnsQueryClass": {
            "data_type": "Integer",
            "description": "The DNS class ID. In practice, only the IN class (ID 1) is used, and therefore this field is less valuable.",
            "class": "Optional",
        },
        "DnsQueryClassName": {
            "data_type": "String",
            "description": "The DNS class name. In practice, only the IN class (ID 1) is used, and therefore this field is less valuable.Example: IN",
            "class": "Optional",
        },
        "DnsFlags": {
            "data_type": "String",
            "description": 'The flags field, as provided by the reporting device. If flag information is provided in multiple fields, concatenate them with comma as a separator. Since DNS flags are complex to parse and are less often used by analytics, parsing, and normalization aren\'t required. Microsoft Sentinel can use an auxiliary function to provide flags information. For more information, see Handling DNS response. Example: ["DR"]',
            "class": "Optional",
        },
        "DnsNetworkDuration": {
            "data_type": "Integer",
            "description": "The amount of time, in milliseconds, for the completion of DNS request.Example: 1500",
            "class": "Optional",
        },
        "Duration": {"data_type": "", "description": "Alias to DnsNetworkDuration", "class": "Alias"},
        "DnsFlagsAuthenticated": {
            "data_type": "Boolean",
            "description": "The DNS AD flag, which is related to DNSSEC, indicates in a response that all data included in the answer and authority sections of the response have been verified by the server according to the policies of that server. For more information, see RFC 3655 Section 6.1 for more information.",
            "class": "Optional",
        },
        "DnsFlagsAuthoritative": {
            "data_type": "Boolean",
            "description": "The DNS AA flag indicates whether the response from the server was authoritative",
            "class": "Optional",
        },
        "DnsFlagsCheckingDisabled": {
            "data_type": "Boolean",
            "description": "The DNS CD flag, which is related to DNSSEC, indicates in a query that non-verified data is acceptable to the system sending the query. For more information, see RFC 3655 Section 6.1 for more information.",
            "class": "Optional",
        },
        "DnsFlagsRecursionAvailable": {
            "data_type": "Boolean",
            "description": "The DNS RA flag indicates in a response that  that server supports recursive queries.",
            "class": "Optional",
        },
        "DnsFlagsRecursionDesired": {
            "data_type": "Boolean",
            "description": "The DNS RD flag indicates in a request that that client would like the server to use recursive queries.",
            "class": "Optional",
        },
        "DnsFlagsTruncated": {
            "data_type": "Boolean",
            "description": "The DNS TC flag indicates that a response was truncated as it exceeded the maximum response size.",
            "class": "Optional",
        },
        "DnsFlagsZ": {
            "data_type": "Boolean",
            "description": "The DNS Z flag is a deprecated DNS flag, which might be reported by older DNS systems.",
            "class": "Optional",
        },
        "DnsSessionId": {
            "data_type": "string",
            "description": "The DNS session identifier as reported by the reporting device. This value is different from TransactionIdHex, the DNS query unique ID as assigned by the DNS client.Example: EB4BFA28-2EAD-4EF7-BC8A-51DF4FDF5B55",
            "class": "Optional",
        },
        "SessionId": {"data_type": "", "description": "Alias to DnsSessionId", "class": "Alias"},
        "DnsResponseIpCountry": {
            "data_type": "Country",
            "description": "The country associated with one of the IP addresses in the DNS response. For more information, see Logical types.Example: USA",
            "class": "Optional",
        },
        "DnsResponseIpRegion": {
            "data_type": "Region",
            "description": "The region, or state, associated with one of the IP addresses in the DNS response. For more information, see Logical types.Example: Vermont",
            "class": "Optional",
        },
        "DnsResponseIpCity": {
            "data_type": "City",
            "description": "The city associated with one of the IP addresses in the DNS response. For more information, see Logical types.Example: Burlington",
            "class": "Optional",
        },
        "DnsResponseIpLatitude": {
            "data_type": "Latitude",
            "description": "The latitude of the geographical coordinate associated with one of the IP addresses in the DNS response. For more information, see Logical types.Example: 44.475833",
            "class": "Optional",
        },
        "DnsResponseIpLongitude": {
            "data_type": "Longitude",
            "description": "The longitude of the geographical coordinate associated with one of the IP addresses in the DNS response. For more information, see Logical types.Example: 73.211944",
            "class": "Optional",
        },
        "UrlCategory": {
            "data_type": "String",
            "description": "A DNS event source may also look up the category of the requested Domains. The field is called UrlCategory to align with the Microsoft Sentinel network schema. DomainCategory is added as an alias that's fitting to DNS. Example: Educational \\\\ Phishing",
            "class": "Optional",
        },
        "DomainCategory": {"data_type": "", "description": "Alias to UrlCategory.", "class": "Alias"},
        "NetworkRuleName": {
            "data_type": "String",
            "description": "The name or ID of the rule which identified the threat. Example: AnyAnyDrop",
            "class": "Optional",
        },
        "NetworkRuleNumber": {
            "data_type": "Integer",
            "description": "The number of the rule which identified the threat.Example: 23",
            "class": "Optional",
        },
        "Rule": {
            "data_type": "String",
            "description": "Either the value of NetworkRuleName or the value of NetworkRuleNumber. If the value of NetworkRuleNumber is used, the type should be converted to string.",
            "class": "Alias",
        },
        "ThreatId": {
            "data_type": "String",
            "description": "The ID of the threat or malware identified in the network session.Example: Tr.124",
            "class": "Optional",
        },
        "ThreatCategory": {
            "data_type": "String",
            "description": "If a DNS event source also provides DNS security, it may also evaluate the DNS event. For example, it can search for the IP address or domain in a threat intelligence database, and assign the domain or IP address with a Threat Category.",
            "class": "Optional",
        },
        "ThreatIpAddr": {
            "data_type": "IP Address",
            "description": "An IP address for which a threat was identified. The field ThreatField contains the name of the field ThreatIpAddr represents. If a threat is identified in the Domain field, this field should be empty.",
            "class": "Optional",
        },
        "ThreatField": {
            "data_type": "Enumerated",
            "description": "The field for which a threat was identified. The value is either SrcIpAddr, DstIpAddr, Domain, or DnsResponseName.",
            "class": "Conditional",
        },
        "ThreatName": {
            "data_type": "String",
            "description": "The name of the threat identified, as reported by the reporting device.",
            "class": "Optional",
        },
        "ThreatConfidence": {
            "data_type": "Integer",
            "description": "The confidence level of the threat identified, normalized to a value between 0 and a 100.",
            "class": "Optional",
        },
        "ThreatOriginalConfidence": {
            "data_type": "String",
            "description": "The original confidence level of the threat identified, as reported by the reporting device.",
            "class": "Optional",
        },
        "ThreatRiskLevel": {
            "data_type": "Integer",
            "description": "The risk level associated with the threat identified, normalized to a value between 0 and a 100.",
            "class": "Optional",
        },
        "ThreatOriginalRiskLevel": {
            "data_type": "String",
            "description": "The original risk level associated with the threat identified, as reported by the reporting device.",
            "class": "Optional",
        },
        "ThreatIsActive": {
            "data_type": "Boolean",
            "description": "True if the threat identified is considered an active threat.",
            "class": "Optional",
        },
        "ThreatFirstReportedTime": {
            "data_type": "datetime",
            "description": "The first time the IP address or domain were identified as a threat.",
            "class": "Optional",
        },
        "ThreatLastReportedTime": {
            "data_type": "datetime",
            "description": "The last time the IP address or domain were identified as a threat.",
            "class": "Optional",
        },
    },
    "imFileEvent": {
        "EventType": {
            "data_type": "Enumerated",
            "description": "Describes the operation reported by the record. Supported values include: - FileAccessed- FileCreated- FileModified- FileDeleted- FileRenamed- FileCopied- FileMoved- FolderCreated- FolderDeleted- FolderMoved- FolderModified- FileCreatedOrModified",
            "class": "Mandatory",
        },
        "EventSubType": {
            "data_type": "Enumerated",
            "description": "Describes details about the operation reported in EventType. Supported values per event type include:- FileCreated -  Upload, Checkin- FileModified - Checkin- FileCreatedOrModified - Checkin - FileAccessed - Download, Preview, Checkout, Extended- FileDeleted - Recycled, Versions, Site",
            "class": "Optional",
        },
        "EventSchema": {
            "data_type": "String",
            "description": "The name of the schema documented here is FileEvent.",
            "class": "Mandatory",
        },
        "EventSchemaVersion": {
            "data_type": "String",
            "description": "The version of the schema. The version of the schema documented here is 0.2.1",
            "class": "Mandatory",
        },
        "Dvc fields": {
            "data_type": "-",
            "description": "For File activity events, device fields refer to the system on which the file activity occurred.",
            "class": "-",
        },
        "TargetFileCreationTime": {
            "data_type": "Date/Time",
            "description": "The time at which the target file was created.",
            "class": "Optional",
        },
        "TargetFileDirectory": {
            "data_type": "String",
            "description": "The target file folder or location. This field should be similar to the TargetFilePath field, without the final element. Note:  A parser can provide this value if the value available in the log source and does not need to be extracted from the full path.",
            "class": "Optional",
        },
        "TargetFileExtension": {
            "data_type": "String",
            "description": "The target file extension.Note:  A parser can provide this value if the value available in the log source and does not need to be extracted from the full path.",
            "class": "Optional",
        },
        "TargetFileMimeType": {
            "data_type": "Enumerated",
            "description": "The Mime, or Media, type of the target file. Allowed values are listed in the IANA Media Types repository.",
            "class": "Optional",
        },
        "TargetFileName": {
            "data_type": "String",
            "description": "The name of the target file, without a path or a location, but with an extension if relevant. This field should be similar to the final element in the TargetFilePath field.",
            "class": "Recommended",
        },
        "FileName": {"data_type": "", "description": "Alias to the TargetFileName field.", "class": "Alias"},
        "TargetFilePath": {
            "data_type": "String",
            "description": "The full, normalized path of the target file, including the folder or location, the file name, and the extension. For more information, see Path structure. Note: If the record does not include folder or location information, store the filename only here. Example: C:\\Windows\\System32\\notepad.exe",
            "class": "Mandatory",
        },
        "TargetFilePathType": {
            "data_type": "Enumerated",
            "description": "The type of TargetFilePath. For more information, see Path structure.",
            "class": "Mandatory",
        },
        "FilePath": {"data_type": "", "description": "Alias to the TargetFilePath field.", "class": "Alias"},
        "TargetFileMD5": {
            "data_type": "MD5",
            "description": "The MD5 hash of the target file. Example: 75a599802f1fa166cdadb360960b1dd0",
            "class": "Optional",
        },
        "TargetFileSHA1": {
            "data_type": "SHA1",
            "description": "The SHA-1 hash of the target file. Example: d55c5a4df19b46db8c54c801c4665d3338acdab0",
            "class": "Optional",
        },
        "TargetFileSHA256": {
            "data_type": "SHA256",
            "description": "The SHA-256 hash of the target file. Example: e81bb824c4a09a811af17deae22f22dd2e1ec8cbb00b22629d2899f7c68da274",
            "class": "Optional",
        },
        "TargetFileSHA512": {
            "data_type": "SHA512",
            "description": "The SHA-512 hash of the source file.",
            "class": "Optional",
        },
        "Hash": {"data_type": "", "description": "Alias to the best available Target File hash.", "class": "Alias"},
        "HashType": {
            "data_type": "String",
            "description": "The type of hash stored in the HASH alias field, allowed values are MD5, SHA, SHA256, SHA512 and IMPHASH. Mandatory if Hash is populated.",
            "class": "Recommended",
        },
        "TargetFileSize": {
            "data_type": "Long",
            "description": "The size of the target file in bytes.",
            "class": "Optional",
        },
        "SrcFileCreationTime": {
            "data_type": "Date/Time",
            "description": "The time at which the source file was created.",
            "class": "Optional",
        },
        "SrcFileDirectory": {
            "data_type": "String",
            "description": "The source file folder or location. This field should be similar to the SrcFilePath field, without the final element. Note: A parser can provide this value if the value is available in the log source, and does not need to be extracted from the full path.",
            "class": "Optional",
        },
        "SrcFileExtension": {
            "data_type": "String",
            "description": "The source file extension. Note: A parser can provide this value the value is available in the log source, and does not need to be extracted from the full path.",
            "class": "Optional",
        },
        "SrcFileMimeType": {
            "data_type": "Enumerated",
            "description": "The Mime or Media type of the source file. Supported values are listed in the IANA Media Types repository.",
            "class": "Optional",
        },
        "SrcFileName": {
            "data_type": "String",
            "description": "The name of the source file, without a path or a location, but with an extension if relevant. This field should be similar to the last element in the SrcFilePath field.",
            "class": "Recommended",
        },
        "SrcFilePath": {
            "data_type": "String",
            "description": "The full, normalized path of the source file, including the folder or location, the file name, and the extension. For more information, see Path structure.Example: /etc/init.d/networking",
            "class": "Recommended",
        },
        "SrcFilePathType": {
            "data_type": "Enumerated",
            "description": "The type of SrcFilePath. For more information, see Path structure.",
            "class": "Recommended",
        },
        "SrcFileMD5": {
            "data_type": "MD5",
            "description": "The MD5 hash of the source file. Example:           75a599802f1fa166cdadb360960b1dd0",
            "class": "Optional",
        },
        "SrcFileSHA1": {
            "data_type": "SHA1",
            "description": "The SHA-1 hash of the source file.Example:d55c5a4df19b46db8c54c801c4665d3338acdab0",
            "class": "Optional",
        },
        "SrcFileSHA256": {
            "data_type": "SHA256",
            "description": "The SHA-256 hash of the source file. Example: e81bb824c4a09a811af17deae22f22dd2e1ec8cbb00b22629d2899f7c68da274",
            "class": "Optional",
        },
        "SrcFileSHA512": {
            "data_type": "SHA512",
            "description": "The SHA-512 hash of the source file.",
            "class": "Optional",
        },
        "SrcFileSize": {
            "data_type": "Long",
            "description": "The size of the source file in bytes.",
            "class": "Optional",
        },
        "ActorUserId": {
            "data_type": "String",
            "description": "A machine-readable, alphanumeric, unique representation of the Actor. For the supported format for different ID types, refer to the User entity. Example: S-1-12",
            "class": "Recommended",
        },
        "ActorScope": {
            "data_type": "String",
            "description": "The scope, such as Microsoft Entra tenant, in which ActorUserId and ActorUsername are defined. or more information and list of allowed values, see UserScope in the Schema Overview article.",
            "class": "Optional",
        },
        "ActorScopeId": {
            "data_type": "String",
            "description": "The scope ID, such as Microsoft Entra Directory ID, in which ActorUserId and ActorUsername are defined. or more information and list of allowed values, see UserScopeId in the Schema Overview article.",
            "class": "Optional",
        },
        "ActorUserIdType": {
            "data_type": "String",
            "description": "The type of the ID stored in the ActorUserId field. For a list of allowed values and further information, refer to UserIdType in the Schema Overview article.",
            "class": "Conditional",
        },
        "ActorUsername": {
            "data_type": "String",
            "description": "The Actor username, including domain information when available. For the supported format for different ID types, refer to the User entity. Use the simple form only if domain information isn't available.Store the Username type in the ActorUsernameType field. If other username formats are available, store them in the fields ActorUsername<UsernameType>.Example: AlbertE",
            "class": "Mandatory",
        },
        "User": {
            "data_type": "",
            "description": "Alias to the ActorUsername field. Example: CONTOSO\\dadmin",
            "class": "Alias",
        },
        "ActorUsernameType": {
            "data_type": "Enumerated",
            "description": "Specifies the type of the user name stored in the ActorUsername field. For a list of allowed values and further information, refer to UsernameType in the Schema Overview article.Example: Windows",
            "class": "Conditional",
        },
        "ActorSessionId": {
            "data_type": "String",
            "description": "The unique ID of the login session of the Actor.  Example: 999Note: The type is defined as string to support varying systems, but on Windows this value must be numeric. If you are using a Windows machine and used a different type, make sure to convert the values. For example, if you used a hexadecimal value, convert it to a decimal value.",
            "class": "Optional",
        },
        "ActorUserType": {
            "data_type": "UserType",
            "description": "The type of Actor. For a list of allowed values and further information, refer to UserType in the Schema Overview article. Note: The value might be provided in the source record by using different terms, which should be normalized to these values. Store the original value in the ActorOriginalUserType field.",
            "class": "Optional",
        },
        "ActorOriginalUserType": {
            "data_type": "String",
            "description": "The original destination user type, if provided by the reporting device.",
            "class": "Optional",
        },
        "ActingProcessCommandLine": {
            "data_type": "String",
            "description": 'The command line used to run the acting process. Example: "choco.exe" -v',
            "class": "Optional",
        },
        "ActingProcessName": {
            "data_type": "string",
            "description": "The name of the acting process. This name is commonly derived from the image or executable file that's used to define the initial code and data that's mapped into the process' virtual address space.Example: C:\\Windows\\explorer.exe",
            "class": "Optional",
        },
        "Process": {"data_type": "", "description": "Alias to ActingProcessName", "class": "Alias"},
        "ActingProcessId": {
            "data_type": "String",
            "description": "The process ID (PID) of the acting process.Example:  48610176 Note: The type is defined as string to support varying systems, but on Windows and Linux this value must be numeric. If you are using a Windows or Linux machine and used a different type, make sure to convert the values. For example, if you used a hexadecimal value, convert it to a decimal value.",
            "class": "Optional",
        },
        "ActingProcessGuid": {
            "data_type": "string",
            "description": "A generated unique identifier (GUID) of the acting process. Enables identifying the process across systems.   Example: EF3BD0BD-2B74-60C5-AF5C-010000001E00",
            "class": "Optional",
        },
        "SrcIpAddr": {
            "data_type": "IP Address",
            "description": "When the operation is initiated by a remote system, the IP address of this system.Example: 185.175.35.214",
            "class": "Recommended",
        },
        "IpAddr": {"data_type": "", "description": "Alias to SrcIpAddr", "class": "Alias"},
        "Src": {"data_type": "", "description": "Alias to SrcIpAddr", "class": "Alias"},
        "SrcPortNumber": {
            "data_type": "Integer",
            "description": "When the operation is initiated by a remote system, the port number from which the connection was initiated.Example: 2335",
            "class": "Optional",
        },
        "SrcHostname": {
            "data_type": "Hostname",
            "description": "The source device hostname, excluding domain information. If no device name is available, store the relevant IP address in this field.Example: DESKTOP-1282V4D",
            "class": "Recommended",
        },
        "SrcDomain": {
            "data_type": "String",
            "description": "The domain of the source device.Example: Contoso",
            "class": "Recommended",
        },
        "SrcDomainType": {
            "data_type": "DomainType",
            "description": "The type of SrcDomain. For a list of allowed values and further information, refer to DomainType in the Schema Overview article.Required if SrcDomain is used.",
            "class": "Conditional",
        },
        "SrcFQDN": {
            "data_type": "String",
            "description": "The source device hostname, including domain information when available. Note: This field supports both traditional FQDN format and Windows domain\\hostname format. The SrcDomainType field reflects the format used. Example: Contoso\\DESKTOP-1282V4D",
            "class": "Optional",
        },
        "SrcDescription": {
            "data_type": "String",
            "description": "A descriptive text associated with the device. For example: Primary Domain Controller.",
            "class": "Optional",
        },
        "SrcDvcId": {
            "data_type": "String",
            "description": "The ID of the source device. If multiple IDs are available, use the most important one, and store the others in the fields SrcDvc<DvcIdType>.Example: ac7e9755-8eae-4ffc-8a02-50ed7a2216c3",
            "class": "Optional",
        },
        "SrcDvcScopeId": {
            "data_type": "String",
            "description": "The cloud platform scope ID the device belongs to. SrcDvcScopeId map to a subscription ID on Azure and to an account ID on AWS.",
            "class": "Optional",
        },
        "SrcDvcScope": {
            "data_type": "String",
            "description": "The cloud platform scope the device belongs to. SrcDvcScope map to a subscription ID on Azure and to an account ID on AWS.",
            "class": "Optional",
        },
        "SrcDvcIdType": {
            "data_type": "DvcIdType",
            "description": "The type of SrcDvcId. For a list of allowed values and further information, refer to DvcIdType in the Schema Overview article. Note: This field is required if SrcDvcId is used.",
            "class": "Conditional",
        },
        "SrcDeviceType": {
            "data_type": "DeviceType",
            "description": "The type of the source device. For a list of allowed values and further information, refer to DeviceType in the Schema Overview article.",
            "class": "Optional",
        },
        "SrcSubscriptionId": {
            "data_type": "String",
            "description": "The cloud platform subscription ID the source device belongs to. SrcSubscriptionId map to a subscription ID on Azure and to an account ID on AWS.",
            "class": "Optional",
        },
        "SrcGeoCountry": {
            "data_type": "Country",
            "description": "The country associated with the source IP address.Example: USA",
            "class": "Optional",
        },
        "SrcGeoRegion": {
            "data_type": "Region",
            "description": "The region associated with the source IP address.Example: Vermont",
            "class": "Optional",
        },
        "SrcGeoCity": {
            "data_type": "City",
            "description": "The city associated with the source IP address.Example: Burlington",
            "class": "Optional",
        },
        "SrcGeoLatitude": {
            "data_type": "Latitude",
            "description": "The latitude of the geographical coordinate associated with the source IP address.Example: 44.475833",
            "class": "Optional",
        },
        "SrcGeoLongitude": {
            "data_type": "Longitude",
            "description": "The longitude of the geographical coordinate associated with the source IP address.Example: 73.211944",
            "class": "Optional",
        },
        "HttpUserAgent": {
            "data_type": "String",
            "description": "When the operation is initiated by a remote system using HTTP or HTTPS, the user agent used.For example:Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135Safari/537.36 Edge/12.246",
            "class": "Optional",
        },
        "NetworkApplicationProtocol": {
            "data_type": "String",
            "description": "When the operation is initiated by a remote system, this value is the application layer protocol used in the OSI model. While this field is not enumerated, and any value is accepted, preferable values include: HTTP, HTTPS, SMB,FTP, and SSHExample: SMB",
            "class": "Optional",
        },
        "TargetAppName": {
            "data_type": "String",
            "description": "The name of the destination application.Example: Facebook",
            "class": "Optional",
        },
        "Application": {"data_type": "", "description": "Alias to TargetAppName.", "class": "Alias"},
        "TargetAppId": {
            "data_type": "String",
            "description": "The ID of the destination application, as reported by the reporting device.",
            "class": "Optional",
        },
        "TargetAppType": {
            "data_type": "AppType",
            "description": "The type of the destination application. For a list of allowed values and further information, refer to AppType in the Schema Overview article.This field is mandatory if TargetAppName or TargetAppId are used.",
            "class": "Optional",
        },
        "TargetUrl": {
            "data_type": "String",
            "description": "When the operation is initiated using HTTP or HTTPS, the URL used. Example: https://onedrive.live.com/?authkey=...",
            "class": "Optional",
        },
        "Url": {"data_type": "", "description": "Alias to TargetUrl", "class": "Alias"},
        "RuleName": {
            "data_type": "String",
            "description": "The name or ID of the rule by associated with the inspection results.",
            "class": "Optional",
        },
        "RuleNumber": {
            "data_type": "Integer",
            "description": "The number of the rule associated with the inspection results.",
            "class": "Optional",
        },
        "Rule": {
            "data_type": "String",
            "description": "Either the value of kRuleName or the value of RuleNumber. If the value of RuleNumber is used, the type should be converted to string.",
            "class": "Conditional",
        },
        "ThreatId": {
            "data_type": "String",
            "description": "The ID of the threat or malware identified in the file activity.",
            "class": "Optional",
        },
        "ThreatName": {
            "data_type": "String",
            "description": "The name of the threat or malware identified in the file activity.Example: EICAR Test File",
            "class": "Optional",
        },
        "ThreatCategory": {
            "data_type": "String",
            "description": "The category of the threat or malware identified in the file activity.Example: Trojan",
            "class": "Optional",
        },
        "ThreatRiskLevel": {
            "data_type": "Integer",
            "description": "The risk level associated with the identified threat. The level should be a number between 0 and 100.Note: The value might be provided in the source record by using a different scale, which should be normalized to this scale. The original value should be stored in ThreatRiskLevelOriginal.",
            "class": "Optional",
        },
        "ThreatOriginalRiskLevel": {
            "data_type": "String",
            "description": "The risk level as reported by the reporting device.",
            "class": "Optional",
        },
        "ThreatFilePath": {
            "data_type": "String",
            "description": "A file path for which a threat was identified. The field ThreatField contains the name of the field ThreatFilePath represents.",
            "class": "Optional",
        },
        "ThreatField": {
            "data_type": "Enumerated",
            "description": "The field for which a threat was identified. The value is either SrcFilePath or DstFilePath.",
            "class": "Optional",
        },
        "ThreatConfidence": {
            "data_type": "Integer",
            "description": "The confidence level of the threat identified, normalized to a value between 0 and a 100.",
            "class": "Optional",
        },
        "ThreatOriginalConfidence": {
            "data_type": "String",
            "description": "The original confidence level of the threat identified, as reported by the reporting device.",
            "class": "Optional",
        },
        "ThreatIsActive": {
            "data_type": "Boolean",
            "description": "True if the threat identified is considered an active threat.",
            "class": "Optional",
        },
        "ThreatFirstReportedTime": {
            "data_type": "datetime",
            "description": "The first time the IP address or domain were identified as a threat.",
            "class": "Optional",
        },
        "ThreatLastReportedTime": {
            "data_type": "datetime",
            "description": "The last time the IP address or domain were identified as a threat.",
            "class": "Optional",
        },
    },
    "imNetworkSession": {
        "EventCount": {
            "data_type": "Integer",
            "description": "Netflow sources support aggregation, and the EventCount field should be set to the value of the Netflow FLOWS field. For other sources, the value is typically set to 1.",
            "class": "Mandatory",
        },
        "EventType": {
            "data_type": "Enumerated",
            "description": "Describes the scenario reported by the record. For Network Session records, the allowed values are: - EndpointNetworkSession - NetworkSession  - L2NetworkSession- IDS  - FlowFor more information on event types, refer to the schema overview",
            "class": "Mandatory",
        },
        "EventSubType": {
            "data_type": "String",
            "description": "Additional description of the event type, if applicable.  For Network Session records, supported values include:- Start- EndThis is field is not relevant for Flow events.",
            "class": "Optional",
        },
        "EventResult": {
            "data_type": "Enumerated",
            "description": "If the source device does not provide an event result, EventResult should be based on the value of DvcAction.  If DvcAction is Deny, Drop, Drop ICMP, Reset, Reset Source, or Reset Destination, EventResult should be Failure. Otherwise, EventResult should be Success.",
            "class": "Mandatory",
        },
        "EventResultDetails": {
            "data_type": "Enumerated",
            "description": "Reason or details for the result reported in the EventResult field. Supported values are: - Failover  - Invalid TCP  - Invalid Tunnel - Maximum Retry - Reset - Routing issue - Simulation - Terminated - Timeout - Transient error - Unknown - NA.The original, source specific, value is stored in the EventOriginalResultDetails field.",
            "class": "Recommended",
        },
        "EventSchema": {
            "data_type": "String",
            "description": "The name of the schema documented here is NetworkSession.",
            "class": "Mandatory",
        },
        "EventSchemaVersion": {
            "data_type": "String",
            "description": "The version of the schema. The version of the schema documented here is 0.2.6.",
            "class": "Mandatory",
        },
        "DvcAction": {
            "data_type": "Enumerated",
            "description": "The action taken on the network session. Supported values are:- Allow- Deny- Drop- Drop ICMP- Reset- Reset Source- Reset Destination- Encrypt- Decrypt- VPNrouteNote: The value might be provided in the source record by using different terms, which should be normalized to these values. The original value should be stored in the DvcOriginalAction field.Example: drop",
            "class": "Recommended",
        },
        "EventSeverity": {
            "data_type": "Enumerated",
            "description": "If the source device does not provide an event severity, EventSeverity should be based on the value of DvcAction.  If DvcAction is Deny, Drop, Drop ICMP, Reset, Reset Source, or Reset Destination, EventSeverity should be Low. Otherwise, EventSeverity should be Informational.",
            "class": "Optional",
        },
        "DvcInterface": {
            "data_type": "",
            "description": "The DvcInterface field should alias either the DvcInboundInterface or the DvcOutboundInterface fields.",
            "class": "",
        },
        "Dvc fields": {
            "data_type": "",
            "description": "For Network Session events, device fields refer to the system reporting the Network Session event.",
            "class": "",
        },
        "NetworkApplicationProtocol": {
            "data_type": "String",
            "description": "The application layer protocol used by the connection or session. The value should be in all uppercase.Example: FTP",
            "class": "Optional",
        },
        "NetworkProtocol": {
            "data_type": "Enumerated",
            "description": "The IP protocol used by the connection or session as listed in IANA protocol assignment, which is typically TCP, UDP, or ICMP.Example: TCP",
            "class": "Optional",
        },
        "NetworkProtocolVersion": {
            "data_type": "Enumerated",
            "description": "The version of NetworkProtocol. When using it to distinguish between IP version, use the values IPv4 and IPv6.",
            "class": "Optional",
        },
        "NetworkDirection": {
            "data_type": "Enumerated",
            "description": "The direction of the connection or session: - For the EventType NetworkSession, Flow or L2NetworkSession, NetworkDirection represents the direction relative to the organization or cloud environment boundary. Supported values are Inbound, Outbound, Local (to the organization), External (to the organization) or NA (Not Applicable). - For the EventType EndpointNetworkSession, NetworkDirection represents the direction relative to the endpoint. Supported values are Inbound, Outbound, Local (to the system), Listen or NA (Not Applicable). The Listen value indicates that a device has started accepting network connections but isn't actually, necessarily, connected.",
            "class": "Optional",
        },
        "NetworkDuration": {
            "data_type": "Integer",
            "description": "The amount of time, in milliseconds, for the completion of the network session or connection.Example: 1500",
            "class": "Optional",
        },
        "Duration": {"data_type": "", "description": "Alias to NetworkDuration.", "class": "Alias"},
        "NetworkIcmpType": {
            "data_type": "String",
            "description": "For an ICMP message, ICMP type name associated with the numerical value, as described in RFC 2780 for IPv4 network connections, or in RFC 4443 for IPv6 network connections.Example: Destination Unreachable for NetworkIcmpCode 3",
            "class": "Optional",
        },
        "NetworkIcmpCode": {
            "data_type": "Integer",
            "description": "For an ICMP message, the ICMP code number as described in RFC 2780 for IPv4 network connections, or in RFC 4443 for IPv6 network connections.",
            "class": "Optional",
        },
        "NetworkConnectionHistory": {
            "data_type": "String",
            "description": "TCP flags and other potential IP header information.",
            "class": "Optional",
        },
        "DstBytes": {
            "data_type": "Long",
            "description": "The number of bytes sent from the destination to the source for the connection or session. If the event is aggregated, DstBytes should be the sum over all aggregated sessions.Example: 32455",
            "class": "Recommended",
        },
        "SrcBytes": {
            "data_type": "Long",
            "description": "The number of bytes sent from the source to the destination for the connection or session. If the event is aggregated, SrcBytes should be the sum over all aggregated sessions.Example: 46536",
            "class": "Recommended",
        },
        "NetworkBytes": {
            "data_type": "Long",
            "description": "Number of bytes sent in both directions. If both BytesReceived and BytesSent exist, BytesTotal should equal their sum. If the event is aggregated, NetworkBytes should be the sum over all aggregated sessions.Example: 78991",
            "class": "Optional",
        },
        "DstPackets": {
            "data_type": "Long",
            "description": "The number of packets sent from the destination to the source for the connection or session. The meaning of a packet is defined by the reporting device. If the event is aggregated, DstPackets should be the sum over all aggregated sessions.Example: 446",
            "class": "Optional",
        },
        "SrcPackets": {
            "data_type": "Long",
            "description": "The number of packets sent from the source to the destination for the connection or session. The meaning of a packet is defined by the reporting device. If the event is aggregated, SrcPackets should be the sum over all aggregated sessions.Example: 6478",
            "class": "Optional",
        },
        "NetworkPackets": {
            "data_type": "Long",
            "description": "The number of packets sent in both directions. If both PacketsReceived and PacketsSent exist, BytesTotal should equal their sum. The meaning of a packet is defined by the reporting device. If the event is aggregated, NetworkPackets should be the sum over all aggregated sessions.Example: 6924",
            "class": "Optional",
        },
        "NetworkSessionId": {
            "data_type": "string",
            "description": "The session identifier as reported by the reporting device. Example: 172\\_12\\_53\\_32\\_4322\\_\\_123\\_64\\_207\\_1\\_80",
            "class": "Optional",
        },
        "SessionId": {"data_type": "String", "description": "Alias to NetworkSessionId.", "class": "Alias"},
        "TcpFlagsAck": {
            "data_type": "Boolean",
            "description": "The TCP ACK Flag reported. The acknowledgment flag is used to acknowledge the successful receipt of a packet. As we can see from the diagram above, the receiver sends an ACK and a SYN in the second step of the three way handshake process to tell the sender that it received its initial packet.",
            "class": "Optional",
        },
        "TcpFlagsFin": {
            "data_type": "Boolean",
            "description": "The TCP FIN Flag reported. The finished flag means there is no more data from the sender. Therefore, it is used in the last packet sent from the sender.",
            "class": "Optional",
        },
        "TcpFlagsSyn": {
            "data_type": "Boolean",
            "description": "The TCP SYN Flag reported. The synchronization flag is used as a first step in establishing a three way handshake between two hosts. Only the first packet from both the sender and receiver should have this flag set.",
            "class": "Optional",
        },
        "TcpFlagsUrg": {
            "data_type": "Boolean",
            "description": "The TCP URG Flag reported. The urgent flag is used to notify the receiver to process the urgent packets before processing all other packets. The receiver will be notified when all known urgent data has been received. See RFC 6093 for more details.",
            "class": "Optional",
        },
        "TcpFlagsPsh": {
            "data_type": "Boolean",
            "description": "The TCP PSH Flag reported. The push flag is similar to the URG flag and tells the receiver to process these packets as they are received instead of buffering them.",
            "class": "Optional",
        },
        "TcpFlagsRst": {
            "data_type": "Boolean",
            "description": "The TCP RST Flag reported. The reset flag gets sent from the receiver to the sender when a packet is sent to a particular host that was not expecting it.",
            "class": "Optional",
        },
        "TcpFlagsEce": {
            "data_type": "Boolean",
            "description": "The TCP ECE Flag reported. This flag is responsible for indicating if the TCP peer is ECN capable. See RFC 3168 for more details.",
            "class": "Optional",
        },
        "TcpFlagsCwr": {
            "data_type": "Boolean",
            "description": "The TCP CWR Flag reported. The congestion window reduced flag is used by the sending host to indicate it received a packet with the ECE flag set. See RFC 3168 for more details.",
            "class": "Optional",
        },
        "TcpFlagsNs": {
            "data_type": "Boolean",
            "description": "The TCP NS Flag reported. The nonce sum flag is still an experimental flag used to help protect against accidental malicious concealment of packets from the sender. See RFC 3540 for more details",
            "class": "Optional",
        },
        "Dst": {
            "data_type": "Alias",
            "description": "A unique identifier of the server receiving the DNS request. This field might alias the DstDvcId, DstHostname, or DstIpAddr fields. Example: 192.168.12.1",
            "class": "Recommended",
        },
        "DstIpAddr": {
            "data_type": "IP address",
            "description": "The IP address of the connection or session destination. If the session uses network address translation, DstIpAddr is the publicly visible address, and not the original address of the source, which is stored in DstNatIpAddrExample: 2001:db8::ff00:42:8329Note: This value is mandatory if DstHostname is specified.",
            "class": "Recommended",
        },
        "DstPortNumber": {
            "data_type": "Integer",
            "description": "The destination IP port.Example: 443",
            "class": "Optional",
        },
        "DstHostname": {
            "data_type": "Hostname",
            "description": "The destination device hostname, excluding domain information. If no device name is available, store the relevant IP address in this field.Example: DESKTOP-1282V4D",
            "class": "Recommended",
        },
        "DstDomain": {
            "data_type": "String",
            "description": "The domain of the destination device.Example: Contoso",
            "class": "Recommended",
        },
        "DstDomainType": {
            "data_type": "Enumerated",
            "description": "The type of DstDomain. For a list of allowed values and further information, refer to DomainType in the Schema Overview article.Required if DstDomain is used.",
            "class": "Conditional",
        },
        "DstFQDN": {
            "data_type": "String",
            "description": "The destination device hostname, including domain information when available. Example: Contoso\\DESKTOP-1282V4D Note: This field supports both traditional FQDN format and Windows domain\\hostname format. The DstDomainType reflects the format used.",
            "class": "Optional",
        },
        "DstDvcId": {
            "data_type": "String",
            "description": "The ID of the destination device. If multiple IDs are available, use the most important one, and store the others in the fields DstDvc<DvcIdType>. Example: ac7e9755-8eae-4ffc-8a02-50ed7a2216c3",
            "class": "Optional",
        },
        "DstDvcScopeId": {
            "data_type": "String",
            "description": "The cloud platform scope ID the device belongs to. DstDvcScopeId map to a subscription ID on Azure and to an account ID on AWS.",
            "class": "Optional",
        },
        "DstDvcScope": {
            "data_type": "String",
            "description": "The cloud platform scope the device belongs to. DstDvcScope map to a subscription ID on Azure and to an account ID on AWS.",
            "class": "Optional",
        },
        "DstDvcIdType": {
            "data_type": "Enumerated",
            "description": "The type of DstDvcId. For a list of allowed values and further information, refer to DvcIdType in the Schema Overview article. Required if DstDeviceId is used.",
            "class": "Conditional",
        },
        "DstDeviceType": {
            "data_type": "Enumerated",
            "description": "The type of the destination device.  For a list of allowed values and further information, refer to DeviceType in the Schema Overview article.",
            "class": "Optional",
        },
        "DstZone": {
            "data_type": "String",
            "description": "The network zone of the destination, as defined by the reporting device.Example: Dmz",
            "class": "Optional",
        },
        "DstInterfaceName": {
            "data_type": "String",
            "description": "The network interface used for the connection or session by the destination device.Example: Microsoft Hyper-V Network Adapter",
            "class": "Optional",
        },
        "DstInterfaceGuid": {
            "data_type": "String",
            "description": "The GUID of the network interface used on the destination device.Example:46ad544b-eaf0-47ef-827c-266030f545a6",
            "class": "Optional",
        },
        "DstMacAddr": {
            "data_type": "String",
            "description": "The MAC address of the network interface used for the connection or session by the destination device.Example: 06:10:9f:eb:8f:14",
            "class": "Optional",
        },
        "DstVlanId": {
            "data_type": "String",
            "description": "The VLAN ID related to the destination device.Example: 130",
            "class": "Optional",
        },
        "OuterVlanId": {
            "data_type": "Alias",
            "description": "Alias to DstVlanId. In many cases, the VLAN can't be determined as a source or a destination but is characterized as inner or outer. This alias to signifies that DstVlanId should be used when the VLAN is characterized as outer.",
            "class": "Optional",
        },
        "DstSubscriptionId": {
            "data_type": "String",
            "description": "The cloud platform subscription ID the destination device belongs to. DstSubscriptionId map to a subscription ID on Azure and to an account ID on AWS.",
            "class": "Optional",
        },
        "DstGeoCountry": {
            "data_type": "Country",
            "description": "The country associated with the destination IP address. For more information, see Logical types.Example: USA",
            "class": "Optional",
        },
        "DstGeoRegion": {
            "data_type": "Region",
            "description": "The region, or state, associated with the destination IP address. For more information, see Logical types.Example: Vermont",
            "class": "Optional",
        },
        "DstGeoCity": {
            "data_type": "City",
            "description": "The city associated with the destination IP address. For more information, see Logical types.Example: Burlington",
            "class": "Optional",
        },
        "DstGeoLatitude": {
            "data_type": "Latitude",
            "description": "The latitude of the geographical coordinate associated with the destination IP address. For more information, see Logical types.Example: 44.475833",
            "class": "Optional",
        },
        "DstGeoLongitude": {
            "data_type": "Longitude",
            "description": "The longitude of the geographical coordinate associated with the destination IP address. For more information, see Logical types.Example: 73.211944",
            "class": "Optional",
        },
        "DstUserId": {
            "data_type": "String",
            "description": "A machine-readable, alphanumeric, unique representation of the destination user. For the supported format for different ID types, refer to the User entity. Example: S-1-12",
            "class": "Optional",
        },
        "DstUserScope": {
            "data_type": "String",
            "description": "The scope, such as Microsoft Entra tenant, in which DstUserId and DstUsername are defined. or more information and list of allowed values, see UserScope in the Schema Overview article.",
            "class": "Optional",
        },
        "DstUserScopeId": {
            "data_type": "String",
            "description": "The scope ID, such as Microsoft Entra Directory ID, in which DstUserId and DstUsername are defined. for more information and list of allowed values, see UserScopeId in the Schema Overview article.",
            "class": "Optional",
        },
        "DstUserIdType": {
            "data_type": "UserIdType",
            "description": "The type of the ID stored in the DstUserId field. For a list of allowed values and further information, refer to UserIdType in the Schema Overview article.",
            "class": "Conditional",
        },
        "DstUsername": {
            "data_type": "String",
            "description": "The destination username, including domain information when available. For the supported format for different ID types, refer to the User entity. Use the simple form only if domain information isn't available.Store the Username type in the DstUsernameType field. If other username formats are available, store them in the fields DstUsername<UsernameType>.Example: AlbertE",
            "class": "Optional",
        },
        "User": {"data_type": "", "description": "Alias to DstUsername.", "class": "Alias"},
        "DstUsernameType": {
            "data_type": "UsernameType",
            "description": "Specifies the type of the username stored in the DstUsername field. For a list of allowed values and further information, refer to UsernameType in the Schema Overview article.Example: Windows",
            "class": "Conditional",
        },
        "DstUserType": {
            "data_type": "UserType",
            "description": "The type of destination user. For a list of allowed values and further information, refer to UserType in the Schema Overview article. Note: The value might be provided in the source record by using different terms, which should be normalized to these values. Store the original value in the DstOriginalUserType field.",
            "class": "Optional",
        },
        "DstOriginalUserType": {
            "data_type": "String",
            "description": "The original destination user type, if provided by the source.",
            "class": "Optional",
        },
        "DstAppName": {
            "data_type": "String",
            "description": "The name of the destination application.Example: Facebook",
            "class": "Optional",
        },
        "DstAppId": {
            "data_type": "String",
            "description": "The ID of the destination application, as reported by the reporting device.If DstAppType is Process, DstAppId and DstProcessId should have the same value.Example: 124",
            "class": "Optional",
        },
        "DstAppType": {
            "data_type": "AppType",
            "description": "The type of the destination application. For a list of allowed values and further information, refer to AppType in the Schema Overview article.This field is mandatory if DstAppName or DstAppId are used.",
            "class": "Optional",
        },
        "DstProcessName": {
            "data_type": "String",
            "description": "The file name of the process that terminated the network session. This name is typically considered to be the process name.  Example: C:\\Windows\\explorer.exe",
            "class": "Optional",
        },
        "Process": {
            "data_type": "",
            "description": "Alias to the DstProcessName Example: C:\\Windows\\System32\\rundll32.exe",
            "class": "Alias",
        },
        "DstProcessId": {
            "data_type": "String",
            "description": "The process ID (PID) of the process that terminated the network session.Example:  48610176 Note: The type is defined as string to support varying systems, but on Windows and Linux this value must be numeric. If you are using a Windows or Linux machine and used a different type, make sure to convert the values. For example, if you used a hexadecimal value, convert it to a decimal value.",
            "class": "Optional",
        },
        "DstProcessGuid": {
            "data_type": "String",
            "description": "A generated unique identifier (GUID) of the process that terminated the network session.    Example: EF3BD0BD-2B74-60C5-AF5C-010000001E00",
            "class": "Optional",
        },
        "Src": {
            "data_type": "",
            "description": "A unique identifier of the source device. This field might alias the SrcDvcId, SrcHostname, or SrcIpAddr fields. Example: 192.168.12.1",
            "class": "Alias",
        },
        "SrcIpAddr": {
            "data_type": "IP address",
            "description": "The IP address from which the connection or session originated. This value is mandatory if SrcHostname is specified. If the session uses network address translation, SrcIpAddr is the publicly visible address, and not the original address of the source, which is stored in SrcNatIpAddrExample: 77.138.103.108",
            "class": "Recommended",
        },
        "SrcPortNumber": {
            "data_type": "Integer",
            "description": "The IP port from which the connection originated. Might not be relevant for a session comprising multiple connections.Example: 2335",
            "class": "Optional",
        },
        "SrcHostname": {
            "data_type": "Hostname",
            "description": "The source device hostname, excluding domain information. If no device name is available, store the relevant IP address in this field.Example: DESKTOP-1282V4D",
            "class": "Recommended",
        },
        "SrcDomain": {
            "data_type": "String",
            "description": "The domain of the source device.Example: Contoso",
            "class": "Recommended",
        },
        "SrcDomainType": {
            "data_type": "DomainType",
            "description": "The type of SrcDomain. For a list of allowed values and further information, refer to DomainType in the Schema Overview article.Required if SrcDomain is used.",
            "class": "Conditional",
        },
        "SrcFQDN": {
            "data_type": "String",
            "description": "The source device hostname, including domain information when available. Note: This field supports both traditional FQDN format and Windows domain\\hostname format. The SrcDomainType field reflects the format used. Example: Contoso\\DESKTOP-1282V4D",
            "class": "Optional",
        },
        "SrcDvcId": {
            "data_type": "String",
            "description": "The ID of the source device. If multiple IDs are available, use the most important one, and store the others in the fields SrcDvc<DvcIdType>.Example: ac7e9755-8eae-4ffc-8a02-50ed7a2216c3",
            "class": "Optional",
        },
        "SrcDvcScopeId": {
            "data_type": "String",
            "description": "The cloud platform scope ID the device belongs to. SrcDvcScopeId map to a subscription ID on Azure and to an account ID on AWS.",
            "class": "Optional",
        },
        "SrcDvcScope": {
            "data_type": "String",
            "description": "The cloud platform scope the device belongs to. SrcDvcScope map to a subscription ID on Azure and to an account ID on AWS.",
            "class": "Optional",
        },
        "SrcDvcIdType": {
            "data_type": "DvcIdType",
            "description": "The type of SrcDvcId. For a list of allowed values and further information, refer to DvcIdType in the Schema Overview article. Note: This field is required if SrcDvcId is used.",
            "class": "Conditional",
        },
        "SrcDeviceType": {
            "data_type": "DeviceType",
            "description": "The type of the source device. For a list of allowed values and further information, refer to DeviceType in the Schema Overview article.",
            "class": "Optional",
        },
        "SrcZone": {
            "data_type": "String",
            "description": "The network zone of the source, as defined by the reporting device.Example: Internet",
            "class": "Optional",
        },
        "SrcInterfaceName": {
            "data_type": "String",
            "description": "The network interface used for the connection or session by the source device. Example: eth01",
            "class": "Optional",
        },
        "SrcInterfaceGuid": {
            "data_type": "String",
            "description": "The GUID of the network interface used on the source device.Example:46ad544b-eaf0-47ef-827c-266030f545a6",
            "class": "Optional",
        },
        "SrcMacAddr": {
            "data_type": "String",
            "description": "The MAC address of the network interface from which the connection or session originated.Example: 06:10:9f:eb:8f:14",
            "class": "Optional",
        },
        "SrcVlanId": {
            "data_type": "String",
            "description": "The VLAN ID related to the source device.Example: 130",
            "class": "Optional",
        },
        "InnerVlanId": {
            "data_type": "Alias",
            "description": "Alias to SrcVlanId. In many cases, the VLAN can't be determined as a source or a destination but is characterized as inner or outer. This alias to signifies that SrcVlanId should be used when the VLAN is characterized as inner.",
            "class": "Optional",
        },
        "SrcSubscriptionId": {
            "data_type": "String",
            "description": "The cloud platform subscription ID the source device belongs to. SrcSubscriptionId map to a subscription ID on Azure and to an account ID on AWS.",
            "class": "Optional",
        },
        "SrcGeoCountry": {
            "data_type": "Country",
            "description": "The country associated with the source IP address.Example: USA",
            "class": "Optional",
        },
        "SrcGeoRegion": {
            "data_type": "Region",
            "description": "The region associated with the source IP address.Example: Vermont",
            "class": "Optional",
        },
        "SrcGeoCity": {
            "data_type": "City",
            "description": "The city associated with the source IP address.Example: Burlington",
            "class": "Optional",
        },
        "SrcGeoLatitude": {
            "data_type": "Latitude",
            "description": "The latitude of the geographical coordinate associated with the source IP address.Example: 44.475833",
            "class": "Optional",
        },
        "SrcGeoLongitude": {
            "data_type": "Longitude",
            "description": "The longitude of the geographical coordinate associated with the source IP address.Example: 73.211944",
            "class": "Optional",
        },
        "SrcUserId": {
            "data_type": "String",
            "description": "A machine-readable, alphanumeric, unique representation of the source user. For the supported format for different ID types, refer to the User entity. Example: S-1-12",
            "class": "Optional",
        },
        "SrcUserScope": {
            "data_type": "String",
            "description": "The scope, such as Microsoft Entra tenant, in which SrcUserId and SrcUsername are defined. or more information and list of allowed values, see UserScope in the Schema Overview article.",
            "class": "Optional",
        },
        "SrcUserScopeId": {
            "data_type": "String",
            "description": "The scope ID, such as Microsoft Entra Directory ID, in which SrcUserId and SrcUsername are defined. for more information and list of allowed values, see UserScopeId in the Schema Overview article.",
            "class": "Optional",
        },
        "SrcUserIdType": {
            "data_type": "UserIdType",
            "description": "The type of the ID stored in the SrcUserId field. For a list of allowed values and further information, refer to UserIdType in the Schema Overview article.",
            "class": "Conditional",
        },
        "SrcUsername": {
            "data_type": "String",
            "description": "The source username, including domain information when available. For the supported format for different ID types, refer to the User entity. Use the simple form only if domain information isn't available.Store the Username type in the SrcUsernameType field. If other username formats are available, store them in the fields SrcUsername<UsernameType>.Example: AlbertE",
            "class": "Optional",
        },
        "SrcUsernameType": {
            "data_type": "UsernameType",
            "description": "Specifies the type of the username stored in the SrcUsername field. For a list of allowed values and further information, refer to UsernameType in the Schema Overview article.Example: Windows",
            "class": "Conditional",
        },
        "SrcUserType": {
            "data_type": "UserType",
            "description": "The type of source user. For a list of allowed values and further information, refer to UserType in the Schema Overview article. Note: The value might be provided in the source record by using different terms, which should be normalized to these values. Store the original value in the SrcOriginalUserType field.",
            "class": "Optional",
        },
        "SrcOriginalUserType": {
            "data_type": "String",
            "description": "The original destination user type, if provided by the reporting device.",
            "class": "Optional",
        },
        "SrcAppName": {
            "data_type": "String",
            "description": "The name of the source application. Example: filezilla.exe",
            "class": "Optional",
        },
        "SrcAppId": {
            "data_type": "String",
            "description": "The ID of the source application, as reported by the reporting device. If SrcAppType is Process, SrcAppId and SrcProcessId should have the same value.Example: 124",
            "class": "Optional",
        },
        "SrcAppType": {
            "data_type": "AppType",
            "description": "The type of the source application. For a list of allowed values and further information, refer to AppType in the Schema Overview article.This field is mandatory if SrcAppName or SrcAppId are used.",
            "class": "Optional",
        },
        "SrcProcessName": {
            "data_type": "String",
            "description": "The file name of the process that initiated the network session. This name is typically considered to be the process name.  Example: C:\\Windows\\explorer.exe",
            "class": "Optional",
        },
        "SrcProcessId": {
            "data_type": "String",
            "description": "The process ID (PID) of the process that initiated the network session.Example:  48610176 Note: The type is defined as string to support varying systems, but on Windows and Linux this value must be numeric. If you are using a Windows or Linux machine and used a different type, make sure to convert the values. For example, if you used a hexadecimal value, convert it to a decimal value.",
            "class": "Optional",
        },
        "SrcProcessGuid": {
            "data_type": "String",
            "description": "A generated unique identifier (GUID) of the process that initiated the network session.  Example: EF3BD0BD-2B74-60C5-AF5C-010000001E00",
            "class": "Optional",
        },
        "Hostname": {
            "data_type": "",
            "description": "- If the event type is NetworkSession, Flow or L2NetworkSession, Hostname is an alias to DstHostname. - If the event type is EndpointNetworkSession, Hostname is an alias to RemoteHostname, which can alias either DstHostname or SrcHostName, depending on NetworkDirection",
            "class": "Alias",
        },
        "IpAddr": {
            "data_type": "",
            "description": "- If the event type is NetworkSession, Flow or L2NetworkSession, IpAddr is an alias to SrcIpAddr. - If the event type is EndpointNetworkSession, IpAddr is an alias to LocalIpAddr, which can alias either SrcIpAddr or DstIpAddr, depending on NetworkDirection.",
            "class": "Alias",
        },
        "DstNatIpAddr": {
            "data_type": "IP address",
            "description": "The DstNatIpAddr represents either of: - The original address of the destination device if network address translation was used. - The IP address used by the intermediary device for communication with the source.Example: 2::1",
            "class": "Optional",
        },
        "DstNatPortNumber": {
            "data_type": "Integer",
            "description": "If reported by an intermediary NAT device, the port used by the NAT device for communication with the source.Example: 443",
            "class": "Optional",
        },
        "SrcNatIpAddr": {
            "data_type": "IP address",
            "description": "The SrcNatIpAddr represents either of: - The original address of the source device if network address translation was used. - The IP address used by the intermediary device for communication with the destination.Example: 4.3.2.1",
            "class": "Optional",
        },
        "SrcNatPortNumber": {
            "data_type": "Integer",
            "description": "If reported by an intermediary NAT device, the port used by the NAT device for communication with the destination.Example: 345",
            "class": "Optional",
        },
        "DvcInboundInterface": {
            "data_type": "String",
            "description": "If reported by an intermediary device, the network interface used by the NAT device for the connection to the source device.Example: eth0",
            "class": "Optional",
        },
        "DvcOutboundInterface": {
            "data_type": "String",
            "description": "If reported by an intermediary device, the network interface used by the NAT device for the connection to the destination device.Example: Ethernet adapter Ethernet 4e",
            "class": "Optional",
        },
        "NetworkRuleName": {
            "data_type": "String",
            "description": "The name or ID of the rule by which DvcAction was decided upon. Example: AnyAnyDrop",
            "class": "Optional",
        },
        "NetworkRuleNumber": {
            "data_type": "Integer",
            "description": "The number of the rule by which DvcAction was decided upon.Example: 23",
            "class": "Optional",
        },
        "Rule": {
            "data_type": "String",
            "description": "Either the value of NetworkRuleName or the value of NetworkRuleNumber. If the value of NetworkRuleNumber is used, the type should be converted to string.",
            "class": "Alias",
        },
        "ThreatId": {
            "data_type": "String",
            "description": "The ID of the threat or malware identified in the network session.Example: Tr.124",
            "class": "Optional",
        },
        "ThreatName": {
            "data_type": "String",
            "description": "The name of the threat or malware identified in the network session.Example: EICAR Test File",
            "class": "Optional",
        },
        "ThreatCategory": {
            "data_type": "String",
            "description": "The category of the threat or malware identified in the network session.Example: Trojan",
            "class": "Optional",
        },
        "ThreatRiskLevel": {
            "data_type": "Integer",
            "description": "The risk level associated with the session. The level should be a number between 0 and 100.Note: The value might be provided in the source record by using a different scale, which should be normalized to this scale. The original value should be stored in ThreatRiskLevelOriginal.",
            "class": "Optional",
        },
        "ThreatOriginalRiskLevel": {
            "data_type": "String",
            "description": "The risk level as reported by the reporting device.",
            "class": "Optional",
        },
        "ThreatIpAddr": {
            "data_type": "IP Address",
            "description": "An IP address for which a threat was identified. The field ThreatField contains the name of the field ThreatIpAddr represents.",
            "class": "Optional",
        },
        "ThreatField": {
            "data_type": "Enumerated",
            "description": "The field for which a threat was identified. The value is either SrcIpAddr or DstIpAddr.",
            "class": "Conditional",
        },
        "ThreatConfidence": {
            "data_type": "Integer",
            "description": "The confidence level of the threat identified, normalized to a value between 0 and a 100.",
            "class": "Optional",
        },
        "ThreatOriginalConfidence": {
            "data_type": "String",
            "description": "The original confidence level of the threat identified, as reported by the reporting device.",
            "class": "Optional",
        },
        "ThreatIsActive": {
            "data_type": "Boolean",
            "description": "True if the threat identified is considered an active threat.",
            "class": "Optional",
        },
        "ThreatFirstReportedTime": {
            "data_type": "datetime",
            "description": "The first time the IP address or domain were identified as a threat.",
            "class": "Optional",
        },
        "ThreatLastReportedTime": {
            "data_type": "datetime",
            "description": "The last time the IP address or domain were identified as a threat.",
            "class": "Optional",
        },
    },
    "imProcessCreate": {
        "EventType": {
            "data_type": "Enumerated",
            "description": "Describes the operation reported by the record. For Process records, supported values include: - ProcessCreated - ProcessTerminated",
            "class": "Mandatory",
        },
        "EventSchemaVersion": {
            "data_type": "String",
            "description": "The version of the schema. The version of the schema documented here is 0.1.4",
            "class": "Mandatory",
        },
        "EventSchema": {
            "data_type": "String",
            "description": "The name of the schema documented here is ProcessEvent.",
            "class": "Optional",
        },
        "Dvc fields": {
            "data_type": "",
            "description": "For process activity events, device fields refer to the system on which the process was executed.",
            "class": "",
        },
        "User": {
            "data_type": "",
            "description": "Alias to the TargetUsername. Example: CONTOSO\\dadmin",
            "class": "Alias",
        },
        "Process": {
            "data_type": "",
            "description": "Alias to the TargetProcessName Example: C:\\Windows\\System32\\rundll32.exe",
            "class": "Alias",
        },
        "CommandLine": {"data_type": "", "description": "Alias to TargetProcessCommandLine", "class": "Alias"},
        "Hash": {
            "data_type": "",
            "description": "Alias to the best available hash for the target process.",
            "class": "Alias",
        },
        "ActorUserId": {
            "data_type": "String",
            "description": "A machine-readable, alphanumeric, unique representation of the Actor. For the supported format for different ID types, refer to the User entity. Example: S-1-12",
            "class": "Recommended",
        },
        "ActorUserIdType": {
            "data_type": "String",
            "description": "The type of the ID stored in the ActorUserId field. For a list of allowed values and further information refer to UserIdType in the Schema Overview article.",
            "class": "Conditional",
        },
        "ActorScope": {
            "data_type": "String",
            "description": "The scope, such as Microsoft Entra tenant, in which ActorUserId and ActorUsername are defined. or more information and list of allowed values, see UserScope in the Schema Overview article.",
            "class": "Optional",
        },
        "ActorUsername": {
            "data_type": "String",
            "description": "The Actor username, including domain information when available. For the supported format for different ID types, refer to the User entity. Use the simple form only if domain information isn't available.Store the Username type in the ActorUsernameType field. If other username formats are available, store them in the fields ActorUsername<UsernameType>.Example: AlbertE",
            "class": "Mandatory",
        },
        "ActorUsernameType": {
            "data_type": "Enumerated",
            "description": "Specifies the type of the user name stored in the ActorUsername field. For a list of allowed values and further information refer to UsernameType in the Schema Overview article.Example: Windows",
            "class": "Conditional",
        },
        "ActorSessionId": {
            "data_type": "String",
            "description": "The unique ID of the login session of the Actor.  Example: 999Note: The type is defined as string to support varying systems, but on Windows this value must be numeric. If you are using a Windows machine and used a different type, make sure to convert the values. For example, if you used a hexadecimal value, convert it to a decimal value.",
            "class": "Optional",
        },
        "ActorUserType": {
            "data_type": "UserType",
            "description": "The type of Actor. For a list of allowed values and further information refer to UserType in the Schema Overview article. Note: The value might be provided in the source record by using different terms, which should be normalized to these values. Store the original value in the ActorOriginalUserType field.",
            "class": "Optional",
        },
        "ActorOriginalUserType": {
            "data_type": "String",
            "description": "The original destination user type, if provided by the reporting device.",
            "class": "Optional",
        },
        "ActingProcessCommandLine": {
            "data_type": "String",
            "description": 'The command line used to run the acting process. Example: "choco.exe" -v',
            "class": "Optional",
        },
        "ActingProcessName": {
            "data_type": "string",
            "description": "The name of the acting process. This name is commonly derived from the image or executable file that's used to define the initial code and data that's mapped into the process' virtual address space.Example: C:\\Windows\\explorer.exe",
            "class": "Optional",
        },
        "ActingProcessFileCompany": {
            "data_type": "String",
            "description": "The company that created the acting process image file.   Example: Microsoft",
            "class": "Optional",
        },
        "ActingProcessFileDescription": {
            "data_type": "String",
            "description": "The description embedded in the version information of the acting process image file. Example:  Notepad++ : a free (GPL) source code editor",
            "class": "Optional",
        },
        "ActingProcessFileProduct": {
            "data_type": "String",
            "description": "The product name from the version information in the acting process image file.  Example: Notepad++",
            "class": "Optional",
        },
        "ActingProcessFileVersion": {
            "data_type": "String",
            "description": "The product version from the version information of the acting process image file. Example: 7.9.5.0",
            "class": "Optional",
        },
        "ActingProcessFileInternalName": {
            "data_type": "String",
            "description": "The product internal file name from the version information of the acting process image file.",
            "class": "Optional",
        },
        "ActingProcessFileOriginalName": {
            "data_type": "String",
            "description": "The product original file name from the version information of the acting process image file.        Example:  Notepad++.exe",
            "class": "Optional",
        },
        "ActingProcessIsHidden": {
            "data_type": "Boolean",
            "description": "An indication of whether the acting process is in hidden mode.",
            "class": "Optional",
        },
        "ActingProcessInjectedAddress": {
            "data_type": "String",
            "description": "The memory address in which the responsible acting process is stored.",
            "class": "Optional",
        },
        "ActingProcessId": {
            "data_type": "String",
            "description": "The process ID (PID) of the acting process.Example:  48610176 Note: The type is defined as string to support varying systems, but on Windows and Linux this value must be numeric. If you are using a Windows or Linux machine and used a different type, make sure to convert the values. For example, if you used a hexadecimal value, convert it to a decimal value.",
            "class": "Mandatory",
        },
        "ActingProcessGuid": {
            "data_type": "string",
            "description": "A generated unique identifier (GUID) of the acting process. Enables identifying the process across systems.   Example: EF3BD0BD-2B74-60C5-AF5C-010000001E00",
            "class": "Optional",
        },
        "ActingProcessIntegrityLevel": {
            "data_type": "String",
            "description": "Every process has an integrity level that is represented in its token. Integrity levels determine the process level of protection or access.  Windows defines the following integrity levels: low, medium, high, and system. Standard users receive a medium integrity level and elevated users receive a high integrity level.  For more information, see Mandatory Integrity Control - Win32 apps.",
            "class": "Optional",
        },
        "ActingProcessMD5": {
            "data_type": "String",
            "description": "The MD5 hash of the acting process image file.  Example:  75a599802f1fa166cdadb360960b1dd0",
            "class": "Optional",
        },
        "ActingProcessSHA1": {
            "data_type": "SHA1",
            "description": "The SHA-1 hash of the acting process image file.               Example: d55c5a4df19b46db8c54c801c4665d3338acdab0",
            "class": "Optional",
        },
        "ActingProcessSHA256": {
            "data_type": "SHA256",
            "description": "The SHA-256 hash of the acting process image file.     Example:  e81bb824c4a09a811af17deae22f22dd2e1ec8cbb00b22629d2899f7c68da274",
            "class": "Optional",
        },
        "ActingProcessSHA512": {
            "data_type": "SHA521",
            "description": "The SHA-512 hash of the acting process image file.",
            "class": "Optional",
        },
        "ActingProcessIMPHASH": {
            "data_type": "String",
            "description": "The Import Hash of all the library DLLs that are used by the acting process.",
            "class": "Optional",
        },
        "ActingProcessCreationTime": {
            "data_type": "DateTime",
            "description": "The date and time when the acting process was started.",
            "class": "Optional",
        },
        "ActingProcessTokenElevation": {
            "data_type": "String",
            "description": "A token indicating the presence or absence of User Access Control (UAC) privilege elevation applied to the acting process.   Example:  None",
            "class": "Optional",
        },
        "ActingProcessFileSize": {
            "data_type": "Long",
            "description": "The size of the file that ran the acting process.",
            "class": "Optional",
        },
        "ParentProcessName": {
            "data_type": "string",
            "description": "The name of the parent process. This name is commonly derived from the image or executable file that's used to define the initial code and data that's mapped into the process' virtual address space.Example: C:\\Windows\\explorer.exe",
            "class": "Optional",
        },
        "ParentProcessFileCompany": {
            "data_type": "String",
            "description": "The name of the company that created the parent process image file.                Example:  Microsoft",
            "class": "Optional",
        },
        "ParentProcessFileDescription": {
            "data_type": "String",
            "description": "The description from the version information in the parent process image file.    Example: Notepad++ : a free (GPL) source code editor",
            "class": "Optional",
        },
        "ParentProcessFileProduct": {
            "data_type": "String",
            "description": "The product name from the version information in parent process image file.      Example:  Notepad++",
            "class": "Optional",
        },
        "ParentProcessFileVersion": {
            "data_type": "String",
            "description": "The product version from the version information in parent process image file.     Example:  7.9.5.0",
            "class": "Optional",
        },
        "ParentProcessIsHidden": {
            "data_type": "Boolean",
            "description": "An indication of whether the parent process is in hidden mode.",
            "class": "Optional",
        },
        "ParentProcessInjectedAddress": {
            "data_type": "String",
            "description": "The memory address in which the responsible parent process is stored.",
            "class": "Optional",
        },
        "ParentProcessId": {
            "data_type": "String",
            "description": "The process ID (PID) of the parent process.        Example:  48610176",
            "class": "Recommended",
        },
        "ParentProcessGuid": {
            "data_type": "String",
            "description": "A generated unique identifier (GUID) of the parent process.  Enables identifying the process across systems.     Example: EF3BD0BD-2B74-60C5-AF5C-010000001E00",
            "class": "Optional",
        },
        "ParentProcessIntegrityLevel": {
            "data_type": "String",
            "description": "Every process has an integrity level that is represented in its token. Integrity levels determine the process level of protection or access.  Windows defines the following integrity levels: low, medium, high, and system. Standard users receive a medium integrity level and elevated users receive a high integrity level.  For more information, see Mandatory Integrity Control - Win32 apps.",
            "class": "Optional",
        },
        "ParentProcessMD5": {
            "data_type": "MD5",
            "description": "The MD5 hash of the parent process image file.  Example: 75a599802f1fa166cdadb360960b1dd0",
            "class": "Optional",
        },
        "ParentProcessSHA1": {
            "data_type": "SHA1",
            "description": "The SHA-1 hash of the parent process image file.        Example:  d55c5a4df19b46db8c54c801c4665d3338acdab0",
            "class": "Optional",
        },
        "ParentProcessSHA256": {
            "data_type": "SHA256",
            "description": "The SHA-256 hash of the parent process image file.        Example:  e81bb824c4a09a811af17deae22f22dd2e1ec8cbb00b22629d2899f7c68da274",
            "class": "Optional",
        },
        "ParentProcessSHA512": {
            "data_type": "SHA512",
            "description": "The SHA-512 hash of the parent process image file.",
            "class": "Optional",
        },
        "ParentProcessIMPHASH": {
            "data_type": "String",
            "description": "The Import Hash of all the library DLLs that are used by the parent process.",
            "class": "Optional",
        },
        "ParentProcessTokenElevation": {
            "data_type": "String",
            "description": "A token indicating the presence or absence of User Access Control (UAC) privilege elevation applied to the parent process.       Example: None",
            "class": "Optional",
        },
        "ParentProcessCreationTime": {
            "data_type": "DateTime",
            "description": "The date and time when the parent process was started.",
            "class": "Optional",
        },
        "TargetUsername": {
            "data_type": "String",
            "description": "The target username, including domain information when available. For the supported format for different ID types, refer to the User entity. Use the simple form only if domain information isn't available.Store the Username type in the TargetUsernameType field. If other username formats are available, store them in the fields TargetUsername<UsernameType>.Example: AlbertE",
            "class": "Mandatory for process create events.",
        },
        "TargetUsernameType": {
            "data_type": "Enumerated",
            "description": "Specifies the type of the user name stored in the TargetUsername field. For a list of allowed values and further information refer to UsernameType in the Schema Overview article.Example: Windows",
            "class": "Conditional",
        },
        "TargetUserId": {
            "data_type": "String",
            "description": "A machine-readable, alphanumeric, unique representation of the target user. For the supported format for different ID types, refer to the User entity. Example: S-1-12",
            "class": "Recommended",
        },
        "TargetUserIdType": {
            "data_type": "String",
            "description": "The type of the ID stored in the TargetUserId field. For a list of allowed values and further information refer to UserIdType in the Schema Overview article.",
            "class": "Conditional",
        },
        "TargetUserSessionId": {
            "data_type": "String",
            "description": "The unique ID of the target user's login session. Example: 999 Note: The type is defined as string to support varying systems, but on Windows this value must be numeric. If you are using a Windows or Linux machine and used a different type, make sure to convert the values. For example, if you used a hexadecimal value, convert it to a decimal value.",
            "class": "Optional",
        },
        "TargetUserType": {
            "data_type": "UserType",
            "description": "The type of Actor. For a list of allowed values and further information refer to UserType in the Schema Overview article. Note: The value might be provided in the source record by using different terms, which should be normalized to these values. Store the original value in the TargetOriginalUserType field.",
            "class": "Optional",
        },
        "TargetOriginalUserType": {
            "data_type": "String",
            "description": "The original destination user type, if provided by the reporting device.",
            "class": "Optional",
        },
        "TargetProcessName": {
            "data_type": "string",
            "description": "The name of the target process. This name is commonly derived from the image or executable file that's used to define the initial code and data that's mapped into the process' virtual address space.        Example:  C:\\Windows\\explorer.exe",
            "class": "Mandatory",
        },
        "TargetProcessFileCompany": {
            "data_type": "String",
            "description": "The name of the company that created the target process image file.      Example:  Microsoft",
            "class": "Optional",
        },
        "TargetProcessFileDescription": {
            "data_type": "String",
            "description": "The description from the version information in the target process image file.   Example:  Notepad++ : a free (GPL) source code editor",
            "class": "Optional",
        },
        "TargetProcessFileProduct": {
            "data_type": "String",
            "description": "The product name from the version information in target process image file.    Example: Notepad++",
            "class": "Optional",
        },
        "TargetProcessFileSize": {
            "data_type": "String",
            "description": "Size of the file that ran the process responsible for the event.",
            "class": "Optional",
        },
        "TargetProcessFileVersion": {
            "data_type": "String",
            "description": "The product version from the version information in the target process image file.     Example: 7.9.5.0",
            "class": "Optional",
        },
        "TargetProcessFileInternalName": {
            "data_type": "String",
            "description": "The product internal file name from the version information of the image file of the target process.",
            "class": "Optional",
        },
        "TargetProcessFileOriginalName": {
            "data_type": "String",
            "description": "The product original file name from the version information of the image file of the target process.",
            "class": "Optional",
        },
        "TargetProcessIsHidden": {
            "data_type": "Boolean",
            "description": "An indication of whether the target process is in hidden mode.",
            "class": "Optional",
        },
        "TargetProcessInjectedAddress": {
            "data_type": "String",
            "description": "The memory address in which the responsible target process is stored.",
            "class": "Optional",
        },
        "TargetProcessMD5": {
            "data_type": "MD5",
            "description": "The MD5 hash of the target process image file.    Example:  75a599802f1fa166cdadb360960b1dd0",
            "class": "Optional",
        },
        "TargetProcessSHA1": {
            "data_type": "SHA1",
            "description": "The SHA-1 hash of the target process image file.         Example:  d55c5a4df19b46db8c54c801c4665d3338acdab0",
            "class": "Optional",
        },
        "TargetProcessSHA256": {
            "data_type": "SHA256",
            "description": "The SHA-256 hash of the target process image file.        Example:  e81bb824c4a09a811af17deae22f22dd2e1ec8cbb00b22629d2899f7c68da274",
            "class": "Optional",
        },
        "TargetProcessSHA512": {
            "data_type": "SHA512",
            "description": "The SHA-512 hash of the target process image file.",
            "class": "Optional",
        },
        "TargetProcessIMPHASH": {
            "data_type": "String",
            "description": "The Import Hash of all the library DLLs that are used by the target process.",
            "class": "Optional",
        },
        "HashType": {
            "data_type": "String",
            "description": "The type of hash stored in the HASH alias field, allowed values are MD5, SHA, SHA256, SHA512 and IMPHASH.",
            "class": "Recommended",
        },
        "TargetProcessCommandLine": {
            "data_type": "String",
            "description": 'The command line used to run the target process.    Example:  "choco.exe" -v',
            "class": "Mandatory",
        },
        "TargetProcessCurrentDirectory": {
            "data_type": "String",
            "description": "The current directory in which the target process is executed.   Example:  c:\\windows\\system32",
            "class": "Optional",
        },
        "TargetProcessCreationTime": {
            "data_type": "DateTime",
            "description": "The product version from the version information of the target process image file.",
            "class": "Recommended",
        },
        "TargetProcessId": {
            "data_type": "String",
            "description": "The process ID (PID) of the target process.     Example: 48610176Note: The type is defined as string to support varying systems, but on Windows and Linux this value must be numeric. If you are using a Windows or Linux machine and used a different type, make sure to convert the values. For example, if you used a hexadecimal value, convert it to a decimal value.",
            "class": "Mandatory",
        },
        "TargetProcessGuid": {
            "data_type": "String",
            "description": "A generated unique identifier (GUID) of the target process. Enables identifying the process across systems.     Example:  EF3BD0BD-2B74-60C5-AF5C-010000001E00",
            "class": "Optional",
        },
        "TargetProcessIntegrityLevel": {
            "data_type": "String",
            "description": "Every process has an integrity level that is represented in its token. Integrity levels determine the process level of protection or access.  Windows defines the following integrity levels: low, medium, high, and system. Standard users receive a medium integrity level and elevated users receive a high integrity level.  For more information, see Mandatory Integrity Control - Win32 apps.",
            "class": "Optional",
        },
        "TargetProcessTokenElevation": {
            "data_type": "String",
            "description": "Token type indicating the presence or absence of User Access Control (UAC) privilege elevation applied to the process that was created or terminated.       Example:  None",
            "class": "Optional",
        },
        "TargetProcessStatusCode": {
            "data_type": "String",
            "description": "The exit code returned by the target process when terminated. This field is valid only for process termination events. For consistency, the field type is string, even if value provided by the operating system is numeric.",
            "class": "Optional",
        },
    },
    "imRegistry": {
        "EventType": {
            "data_type": "Enumerated",
            "description": "Describes the operation reported by the record. For Registry records, supported values include: - RegistryKeyCreated - RegistryKeyDeleted- RegistryKeyRenamed - RegistryValueDeleted - RegistryValueSet",
            "class": "Mandatory",
        },
        "EventSchemaVersion": {
            "data_type": "String",
            "description": "The version of the schema. The version of the schema documented here is 0.1.2",
            "class": "Mandatory",
        },
        "EventSchema": {
            "data_type": "String",
            "description": "The name of the schema documented here is RegistryEvent.",
            "class": "Optional",
        },
        "Dvc fields": {
            "data_type": "",
            "description": "For registry activity events, device fields refer to the system on which the registry activity occurred.",
            "class": "",
        },
        "RegistryKey": {
            "data_type": "String",
            "description": "The registry key associated with the operation, normalized to standard root key naming conventions. For more information, see Root Keys.Registry keys are similar to folders in file systems. For example: HKEY_LOCAL_MACHINE\\SOFTWARE\\MTG",
            "class": "Mandatory",
        },
        "RegistryValue": {
            "data_type": "String",
            "description": "The registry value associated with the operation. Registry values are similar to files in file systems. For example: Path",
            "class": "Recommended",
        },
        "RegistryValueType": {
            "data_type": "String",
            "description": "The type of registry value, normalized to standard form. For more information, see Value Types.For example: Reg_Expand_Sz",
            "class": "Recommended",
        },
        "RegistryValueData": {
            "data_type": "String",
            "description": "The data stored in the registry value. Example: C:\\Windows\\system32;C:\\Windows;",
            "class": "Recommended",
        },
        "RegistryPreviousKey": {
            "data_type": "String",
            "description": "For operations that modify the registry, the original registry key, normalized to standard root key naming. For more information, see Root Keys. Note: If the operation changed other fields, such as the value, but the key remains the same, the RegistryPreviousKey will have the same value as RegistryKey.Example: HKEY_LOCAL_MACHINE\\SOFTWARE\\MTG",
            "class": "Recommended",
        },
        "RegistryPreviousValue": {
            "data_type": "String",
            "description": "For operations that modify the registry, the original value type, normalized to the standard form. For more information, see Value Types. If the type was not changed, this field has the same value as the RegistryValueType field.  Example: Path",
            "class": "Recommended",
        },
        "RegistryPreviousValueType": {
            "data_type": "String",
            "description": "For operations that modify the registry, the original value type. If the type was not changed, this field will have the same value as the RegistryValueType field, normalized to the standard form. For more information, see Value types.Example: Reg_Expand_Sz",
            "class": "Recommended",
        },
        "RegistryPreviousValueData": {
            "data_type": "String",
            "description": "The original registry data, for operations that modify the registry. Example:  C:\\Windows\\system32;C:\\Windows;",
            "class": "Recommended",
        },
        "User": {
            "data_type": "",
            "description": "Alias to the ActorUsername field. Example: CONTOSO\\ dadmin",
            "class": "Alias",
        },
        "Process": {
            "data_type": "",
            "description": "Alias to the ActingProcessName field.Example: C:\\Windows\\System32\\rundll32.exe",
            "class": "Alias",
        },
        "ActorUsername": {
            "data_type": "String",
            "description": "The user name of the user who initiated the event. Example: CONTOSO\\WIN-GG82ULGC9GO$",
            "class": "Mandatory",
        },
        "ActorUsernameType": {
            "data_type": "Enumerated",
            "description": "Specifies the type of the user name stored in the ActorUsername field. For more information, see The User entity. Example: Windows",
            "class": "Conditional",
        },
        "ActorUserId": {
            "data_type": "String",
            "description": "A unique ID of the Actor. The specific ID depends on the system generating the event. For more information, see The User entity.  Example: S-1-5-18",
            "class": "Recommended",
        },
        "ActorScope": {
            "data_type": "String",
            "description": "The scope, such as Microsoft Entra tenant, in which ActorUserId and ActorUsername are defined. or more information and list of allowed values, see UserScope in the Schema Overview article.",
            "class": "Optional",
        },
        "ActorUserIdType": {
            "data_type": "String",
            "description": "The type of the ID stored in the ActorUserId field. For more information, see The User entity. Example: SID",
            "class": "Recommended",
        },
        "ActorSessionId": {
            "data_type": "String",
            "description": "The unique ID of the login session of the Actor.  Example: 999Note: The type is defined as string to support varying systems, but on Windows this value must be numeric. If you are using a Windows machine and the source sends a different type, make sure to convert the value. For example, if source sends a hexadecimal value, convert it to a decimal value.",
            "class": "Conditional",
        },
        "ActingProcessName": {
            "data_type": "String",
            "description": "The file name of the acting process image file. This name is typically considered to be the process name.  Example: C:\\Windows\\explorer.exe",
            "class": "Optional",
        },
        "ActingProcessId": {
            "data_type": "String",
            "description": "The process ID (PID) of the acting process.Example:  48610176 Note: The type is defined as string to support varying systems, but on Windows and Linux this value must be numeric. If you are using a Windows or Linux machine and used a different type, make sure to convert the values. For example, if you used a hexadecimal value, convert it to a decimal value.",
            "class": "Mandatory",
        },
        "ActingProcessGuid": {
            "data_type": "String",
            "description": "A generated unique identifier (GUID) of the acting process.    Example: EF3BD0BD-2B74-60C5-AF5C-010000001E00",
            "class": "Optional",
        },
        "ParentProcessName": {
            "data_type": "String",
            "description": "The file name of the parent process image file. This value is typically considered to be the process name.    Example: C:\\Windows\\explorer.exe",
            "class": "Optional",
        },
        "ParentProcessId": {
            "data_type": "String",
            "description": "The process ID (PID) of the parent process.        Example:  48610176",
            "class": "Mandatory",
        },
        "ParentProcessGuid": {
            "data_type": "String",
            "description": "A generated unique identifier (GUID) of the parent process.      Example: EF3BD0BD-2B74-60C5-AF5C-010000001E00",
            "class": "Optional",
        },
    },
    "imWebSession": {
        "EventType": {
            "data_type": "Enumerated",
            "description": "Describes the operation reported by the record. Allowed values are: - HTTPsession: Denotes a network session used for HTTP or HTTPS, typically reported by an intermediary device, such as a proxy or a Web security gateway. - WebServerSession: Denotes an HTTP request reported by a web server. Such an event typically has less network related information. The URL reported should not include a schema and a server name, but only the path and parameters part of the URL.  - ApiRequest: Denotes an HTTP request reported associated with an API call, typically reported by an application server. Such an event typically has less network related information. When reported by the application server, the URL reported should not include a schema and a server name, but only the path and parameters part of the URL.",
            "class": "Mandatory",
        },
        "EventResult": {
            "data_type": "Enumerated",
            "description": "Describes the event result, normalized to one of the following values:  - Success  - Partial  - Failure  - NA (not applicable) For an HTTP session, Success is defined as a status code lower than 400, and Failure is defined as a status code higher than 400. For a list of HTTP status codes, refer to W3 Org.The source may provide only a value for the EventResultDetails  field, which must be analyzed to get the  EventResult  value.",
            "class": "Mandatory",
        },
        "EventResultDetails": {
            "data_type": "String",
            "description": "The HTTP status code.Note: The value may be provided in the source record using different terms, which should be normalized to these values. The original value should be stored in the EventOriginalResultDetails field.",
            "class": "Recommended",
        },
        "EventSchema": {
            "data_type": "String",
            "description": "The name of the schema documented here is WebSession.",
            "class": "Mandatory",
        },
        "EventSchemaVersion": {
            "data_type": "String",
            "description": "The version of the schema. The version of the schema documented here is 0.2.6",
            "class": "Mandatory",
        },
        "Dvc fields": {
            "data_type": "",
            "description": "For Web Session events,  device fields refer to the system reporting the Web Session event. This is typically an intermediary device for HTTPSession events, and the destination web or application server for WebServerSession and ApiRequest events.",
            "class": "",
        },
        "Url": {
            "data_type": "String",
            "description": "The HTTP request URL, including parameters. For HTTPSession events, the URL may include the schema and should include the server name. For WebServerSession and for ApiRequest the URL would typically not include the schema and server, which can be found in the NetworkApplicationProtocol and DstFQDN fields respectively. Example: https://contoso.com/fo/?k=v&amp;q=u#f",
            "class": "Mandatory",
        },
        "UrlCategory": {
            "data_type": "String",
            "description": "The defined grouping of a URL or the domain part of the URL. The category is commonly provided by web security gateways and is based on the content of the site the URL points to.Example: search engines, adult, news, advertising, and parked domains.",
            "class": "Optional",
        },
        "UrlOriginal": {
            "data_type": "String",
            "description": "The original value of the URL, when the URL was modified by the reporting device and both values are provided.",
            "class": "Optional",
        },
        "HttpVersion": {
            "data_type": "String",
            "description": "The HTTP Request Version.Example: 2.0",
            "class": "Optional",
        },
        "HttpRequestMethod": {
            "data_type": "Enumerated",
            "description": "The HTTP Method. The values are as defined in RFC 7231 and RFC 5789, and include GET, HEAD, POST, PUT, DELETE, CONNECT, OPTIONS, TRACE, and PATCH.Example: GET",
            "class": "Recommended",
        },
        "HttpStatusCode": {
            "data_type": "",
            "description": "The HTTP Status Code. Alias to EventResultDetails.",
            "class": "Alias",
        },
        "HttpContentType": {
            "data_type": "String",
            "description": "The HTTP Response content type header. Note: The HttpContentType field may include both the content format and extra parameters, such as the encoding used to get the actual format. Example: text/html; charset=ISO-8859-4",
            "class": "Optional",
        },
        "HttpContentFormat": {
            "data_type": "String",
            "description": "The content format part of the HttpContentType  Example: text/html",
            "class": "Optional",
        },
        "HttpReferrer": {
            "data_type": "String",
            "description": "The HTTP referrer header.Note: ASIM, in sync with OSSEM, uses the correct spelling for referrer, and not the original HTTP header spelling.Example: https://developer.mozilla.org/docs",
            "class": "Optional",
        },
        "HttpUserAgent": {
            "data_type": "String",
            "description": "The HTTP user agent header.Example: Mozilla/5.0 (Windows NT 10.0; WOW64)AppleWebKit/537.36 (KHTML, like Gecko)Chrome/83.0.4103.97 Safari/537.36",
            "class": "Optional",
        },
        "UserAgent": {"data_type": "", "description": "Alias to HttpUserAgent", "class": "Alias"},
        "HttpRequestXff": {
            "data_type": "IP Address",
            "description": "The HTTP X-Forwarded-For header.Example: 120.12.41.1",
            "class": "Optional",
        },
        "HttpRequestTime": {
            "data_type": "Integer",
            "description": "The amount of time, in milliseconds, it took to send the request to the server, if applicable.Example: 700",
            "class": "Optional",
        },
        "HttpResponseTime": {
            "data_type": "Integer",
            "description": "The amount of time, in milliseconds, it took to receive a response in the server, if applicable.Example: 800",
            "class": "Optional",
        },
        "HttpHost": {
            "data_type": "String",
            "description": "The virtual web server the HTTP request has targeted. This value is typically based on the HTTP Host header.",
            "class": "Optional",
        },
        "FileName": {
            "data_type": "String",
            "description": "For HTTP uploads, the name of the uploaded file.",
            "class": "Optional",
        },
        "FileMD5": {
            "data_type": "MD5",
            "description": "For HTTP uploads, the MD5 hash of the uploaded file.Example: 75a599802f1fa166cdadb360960b1dd0",
            "class": "Optional",
        },
        "FileSHA1": {
            "data_type": "SHA1",
            "description": "For HTTP uploads, the SHA1 hash of the uploaded file.Example:d55c5a4df19b46db8c54c801c4665d3338acdab0",
            "class": "Optional",
        },
        "FileSHA256": {
            "data_type": "SHA256",
            "description": "For HTTP uploads, the SHA256 hash of the uploaded file.Example:e81bb824c4a09a811af17deae22f22dd2e1ec8cbb00b22629d2899f7c68da274",
            "class": "Optional",
        },
        "FileSHA512": {
            "data_type": "SHA512",
            "description": "For HTTP uploads, the SHA512 hash of the uploaded file.",
            "class": "Optional",
        },
        "Hash": {"data_type": "", "description": "Alias to the available Hash field.", "class": "Alias"},
        "FileHashType": {
            "data_type": "Enumerated",
            "description": "The type of the hash in the Hash field. Possible values include: MD5, SHA1, SHA256, and SHA512.",
            "class": "Optional",
        },
        "FileSize": {
            "data_type": "Long",
            "description": "For HTTP uploads, the size in bytes of the uploaded file.",
            "class": "Optional",
        },
        "FileContentType": {
            "data_type": "String",
            "description": "For HTTP uploads, the content type of the uploaded file.",
            "class": "Optional",
        },
    },
}
SENTINEL_ASIM_COMMON_FIELDS = {
    "COMMON": {
        "EventMessage": {
            "data_type": "String",
            "description": "A general message or description, either included in or generated from the record.",
            "class": "Optional",
        },
        "EventCount": {
            "data_type": "Integer",
            "description": "The number of events described by the record. This value is used when the source supports aggregation, and a single record might represent multiple events. For other sources, set to 1.",
            "class": "Mandatory",
        },
        "EventStartTime": {
            "data_type": "Date/time",
            "description": "The time in which the event started. If the source supports aggregation and the record represents multiple events, the time that the first event was generated. If not provided by the source record, this field aliases the TimeGenerated field.",
            "class": "Mandatory",
        },
        "EventEndTime": {
            "data_type": "Date/time",
            "description": "The time in which the event ended. If the source supports aggregation and the record represents multiple events, the time that the last event was generated. If not provided by the source record, this field aliases the TimeGenerated field.",
            "class": "Mandatory",
        },
        "EventType": {
            "data_type": "Enumerated",
            "description": "Describes the operation reported by the record. Each schema documents the list of values valid for this field. The original, source specific, value is stored in the EventOriginalType field.",
            "class": "Mandatory",
        },
        "EventSubType": {
            "data_type": "Enumerated",
            "description": "Describes a subdivision of the operation reported in the EventType field. Each schema documents the list of values valid for this field. The original, source specific, value is stored in the EventOriginalSubType field.",
            "class": "Optional",
        },
        "EventResult": {
            "data_type": "Enumerated",
            "description": "One of the following values: Success, Partial, Failure, NA (Not Applicable). The value might be provided in the source record by using different terms, which should be normalized to these values. Alternatively, the source might provide only the EventResultDetails field, which should be analyzed to derive the EventResult value.Example: Success",
            "class": "Mandatory",
        },
        "EventResultDetails": {
            "data_type": "Enumerated",
            "description": "Reason or details for the result reported in the EventResult field. Each schema documents the list of values valid for this field. The original, source specific, value is stored in the EventOriginalResultDetails field.Example: NXDOMAIN",
            "class": "Recommended",
        },
        "EventUid": {
            "data_type": "String",
            "description": "The unique ID of the record, as assigned by Microsoft Sentinel. This field is typically mapped to the _ItemId Log Analytics field.",
            "class": "Recommended",
        },
        "EventOriginalUid": {
            "data_type": "String",
            "description": "A unique ID of the original record, if provided by the source.Example: 69f37748-ddcd-4331-bf0f-b137f1ea83b",
            "class": "Optional",
        },
        "EventOriginalType": {
            "data_type": "String",
            "description": "The original event type or ID, if provided by the source. For example, this field is used to store the original Windows event ID. This value is used to derive EventType, which should have only one of the values documented for each schema.Example: 4624",
            "class": "Optional",
        },
        "EventOriginalSubType": {
            "data_type": "String",
            "description": "The original event subtype or ID, if provided by the source. For example, this field is used to store the original Windows logon type. This value is used to derive EventSubType, which should have only one of the values documented for each schema.Example: 2",
            "class": "Optional",
        },
        "EventOriginalResultDetails": {
            "data_type": "String",
            "description": "The original result details provided by the source. This value is used to derive EventResultDetails, which should have only one of the values documented for each schema.",
            "class": "Optional",
        },
        "EventSeverity": {
            "data_type": "Enumerated",
            "description": "The severity of the event. Valid values are: Informational, Low, Medium, or High.",
            "class": "Recommended",
        },
        "EventOriginalSeverity": {
            "data_type": "String",
            "description": "The original severity as provided by the reporting device. This value is used to derive EventSeverity.",
            "class": "Optional",
        },
        "EventProduct": {
            "data_type": "String",
            "description": "The product generating the event. The value should be one of the values listed in Vendors and Products.Example: Sysmon",
            "class": "Mandatory",
        },
        "EventProductVersion": {
            "data_type": "String",
            "description": "The version of the product generating the event. Example: 12.1",
            "class": "Optional",
        },
        "EventVendor": {
            "data_type": "String",
            "description": "The vendor of the product generating the event. The value should be one of the values listed in Vendors and Products.Example: Microsoft",
            "class": "Mandatory",
        },
        "EventSchema": {
            "data_type": "String",
            "description": "The schema the event is normalized to. Each schema documents its schema name.",
            "class": "Mandatory",
        },
        "EventSchemaVersion": {
            "data_type": "String",
            "description": "The version of the schema. Each schema documents its current version.",
            "class": "Mandatory",
        },
        "EventReportUrl": {
            "data_type": "String",
            "description": "A URL provided in the event for a resource that provides more information about the event.",
            "class": "Optional",
        },
        "EventOwner": {
            "data_type": "String",
            "description": "The owner of the event, which is usually the department or subsidiary in which it was generated.",
            "class": "Optional",
        },
        "Dvc": {
            "data_type": "String",
            "description": "A unique identifier of the device on which the event occurred or which reported the event, depending on the schema. This field might alias the DvcFQDN, DvcId, DvcHostname, or DvcIpAddr fields. For cloud sources, for which there is no apparent device, use the same value as the Event Product field.",
            "class": "Alias",
        },
        "DvcIpAddr": {
            "data_type": "IP address",
            "description": "The IP address of the device on which the event occurred or which reported the event, depending on the schema. Example: 45.21.42.12",
            "class": "Recommended",
        },
        "DvcHostname": {
            "data_type": "Hostname",
            "description": "The hostname of the device on which the event occurred or which reported the event, depending on the schema. Example: ContosoDc",
            "class": "Recommended",
        },
        "DvcDomain": {
            "data_type": "String",
            "description": "The domain of the device on which the event occurred or which reported the event, depending on the schema.Example: Contoso",
            "class": "Recommended",
        },
        "DvcDomainType": {
            "data_type": "Enumerated",
            "description": "The type of  DvcDomain. For a list of allowed values and further information, refer to DomainType.Note: This field is required if the DvcDomain field is used.",
            "class": "Conditional",
        },
        "DvcFQDN": {
            "data_type": "String",
            "description": "The hostname of the device on which the event occurred or which reported the event, depending on the schema.  Example: Contoso\\DESKTOP-1282V4DNote: This field supports both traditional FQDN format and Windows domain\\hostname format. The  DvcDomainType field reflects the format used.",
            "class": "Optional",
        },
        "DvcDescription": {
            "data_type": "String",
            "description": "A descriptive text associated with the device. For example: Primary Domain Controller.",
            "class": "Optional",
        },
        "DvcId": {
            "data_type": "String",
            "description": "The unique ID of the device on which the event occurred or which reported the event, depending on the schema. Example: 41502da5-21b7-48ec-81c9-baeea8d7d669",
            "class": "Optional",
        },
        "DvcIdType": {
            "data_type": "Enumerated",
            "description": "The type of DvcId. For a list of allowed values and further information, refer to DvcIdType.- MDEidIf multiple IDs are available, use the first one from the list, and store the others by using the field names DvcAzureResourceId and DvcMDEid, respectively.Note: This field is required if the DvcId field is used.",
            "class": "Conditional",
        },
        "DvcMacAddr": {
            "data_type": "MAC",
            "description": "The MAC address of the device on which the event occurred or which reported the event.  Example: 00:1B:44:11:3A:B7",
            "class": "Optional",
        },
        "DvcZone": {
            "data_type": "String",
            "description": "The network on which the event occurred or which reported the event, depending on the schema. The zone is defined by the reporting device.Example: Dmz",
            "class": "Optional",
        },
        "DvcOs": {
            "data_type": "String",
            "description": "The operating system running on the device on which the event occurred or which reported the event.    Example: Windows",
            "class": "Optional",
        },
        "DvcOsVersion": {
            "data_type": "String",
            "description": "The version of the operating system on the device on which the event occurred or which reported the event. Example: 10",
            "class": "Optional",
        },
        "DvcAction": {
            "data_type": "String",
            "description": "For reporting security systems, the action taken by the system, if applicable. Example: Blocked",
            "class": "Recommended",
        },
        "DvcOriginalAction": {
            "data_type": "String",
            "description": "The original DvcAction as provided by the reporting device.",
            "class": "Optional",
        },
        "DvcInterface": {
            "data_type": "String",
            "description": "The network interface on which data was captured. This field is  typically relevant to network related activity, which is captured by an intermediate or tap device.",
            "class": "Optional",
        },
        "DvcScopeId": {
            "data_type": "String",
            "description": "The cloud platform scope ID the device belongs to. DvcScopeId map to a subscription ID on Azure and to an account ID on AWS.",
            "class": "Optional",
        },
        "DvcScope": {
            "data_type": "String",
            "description": "The cloud platform scope the device belongs to. DvcScope map to a subscription ID on Azure and to an account ID on AWS.",
            "class": "Optional",
        },
        "AdditionalFields": {
            "data_type": "Dynamic",
            "description": "If your source provides additional information worth preserving, either keep it with the original field names or create the dynamic AdditionalFields field, and add to it the extra information as key/value pairs.",
            "class": "Optional",
        },
        "ASimMatchingIpAddr": {
            "data_type": "String",
            "description": "When a parser uses the ipaddr_has_any_prefix filtering parameters, this field  is set with the one of the values SrcIpAddr, DstIpAddr, or Both to reflect the matching fields or fields.",
            "class": "Recommended",
        },
        "ASimMatchingHostname": {
            "data_type": "String",
            "description": "When a parser uses the hostname_has_any filtering parameters, this field  is set with the one of the values SrcHostname, DstHostname, or Both to reflect the matching fields or fields.",
            "class": "Recommended",
        },
    },
}

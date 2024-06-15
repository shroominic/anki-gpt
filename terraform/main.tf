provider "azurerm" {
    features { }
}

resource "azurerm_resource_group" "rg" {
  name     = "anki-gpt"
  location = "West US"
}

resource "azurerm_service_plan" "plan" {
  name                = "anki-gpt-plan"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  os_type             = "Linux"
  sku_name            = "B1"
}

resource "azurerm_container_registry" "acr" {
  name                     = "steuerbobacr"
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  sku                      = "Basic"
  admin_enabled            = true
}

resource "azurerm_linux_web_app" "app" {
  name                = "anki-gpt-app"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  service_plan_id     = azurerm_service_plan.plan.id
  public_network_access_enabled = true
  https_only = true

  site_config {
    application_stack {
      docker_image_name = "ankigpt:latest"
      docker_registry_url = "https://${azurerm_container_registry.acr.login_server}"
      docker_registry_username = azurerm_container_registry.acr.admin_username
      docker_registry_password = azurerm_container_registry.acr.admin_password
    }
  }

  app_settings = {
    "WEBSITES_PORT" = "8000"
    "DOCKER_ENABLE_CI" = "true"
    "BASE_URL" = "https://anki-gpt-app.azurewebsites.net"
  }
}

output "public_ip" {
  value = azurerm_linux_web_app.app.default_hostname
}

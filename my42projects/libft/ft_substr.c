/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_substr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ggroff-d <ggroff-d@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/10/26 14:08:42 by ggroff-d          #+#    #+#             */
/*   Updated: 2024/11/06 17:06:44 by ggroff-d         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static char	*ft_strncpy(char *dest, char *src, unsigned int n)
{
	unsigned int	i;

	i = 0;
	while (i < n && src[i] != '\0')
	{
		dest[i] = src[i];
		i++;
	}
	dest[i] = '\0';
	return (dest);
}

char	*ft_substr(char const *s, unsigned int start, size_t len)
{
	char	*new;

	if (s == NULL || ft_strlen((char *)s) == 0
		|| start >= (unsigned int)ft_strlen(s) || len == 0)
	{
		new = (char *)malloc(1 * sizeof(char));
		if (new)
			new[0] = '\0';
		return (new);
	}
	if (start + len >= (unsigned int)ft_strlen(s))
		len = (unsigned int)ft_strlen(s) - start;
	new = (char *)malloc((len + 1) * sizeof(char));
	if (!new)
		return (NULL);
	ft_strncpy(new, (char *)s + start, len);
	new[len] = '\0';
	return (new);
}
